"""
Sphinx extension to add YAML frontmatter to markdown output and restructure
the output for the devportal.

This extension hooks into the sphinx-markdown-builder to:
1. Add frontmatter with a 'title' property to each generated markdown file,
   similar to typedoc-plugin-frontmatter in the TypeScript repo.
2. Restructure the output to have 'api/' and 'guides/' at the root level,
   removing the Sphinx index.md.
"""

import re
import shutil
from pathlib import Path

from sphinx.application import Sphinx
from sphinx.util import logging

logger = logging.getLogger(__name__)


def clean_markdown_title(title: str) -> str:
    """Clean up a title extracted from markdown H1 heading.

    Removes markdown formatting like backticks, links, etc.
    Returns the member/reflection name as-is.

    Examples:
        `get_subscribed_transactions` -> get_subscribed_transactions
        [`algokit_subscriber.subscriber`](#module-algokit_subscriber.subscriber) -> algokit_subscriber.subscriber
    """
    # Remove backticks
    title = title.replace("`", "")

    # Remove markdown links: [text](url) -> text
    title = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", title)

    # Remove any remaining brackets or parentheses at edges
    title = title.strip("[]() ")

    return title


def extract_title_from_content(content: str, filename: str) -> str:
    """Extract a title from the markdown content.

    Uses the first H1 heading as the title, cleaned of markdown formatting.
    Falls back to the filename (without extension) if no H1 found.
    """
    # Try to find first H1 heading
    h1_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    if h1_match:
        return clean_markdown_title(h1_match.group(1).strip())

    # Fall back to filename without extension
    return filename.removesuffix(".md")


def restructure_devportal_output(outdir: Path) -> None:
    """Restructure the devportal output to have api/ and guides/ at root.

    Input structure:
        .devportal/
            index.md
            guides/
            api/algokit_subscriber/

    Output structure:
        .devportal/
            api/  (flattened from api/algokit_subscriber/)
            guides/
    """
    # Move API docs from api/algokit_subscriber/ to api/
    api_subdir = outdir / "api" / "algokit_subscriber"
    api_dir = outdir / "api"

    if api_subdir.exists():
        # Move all files from api/algokit_subscriber/ to api/
        for item in api_subdir.iterdir():
            dest = api_dir / item.name
            if dest.exists():
                if dest.is_dir():
                    shutil.rmtree(dest)
                else:
                    dest.unlink()
            shutil.move(str(item), str(dest))

        # Remove the now-empty algokit_subscriber directory
        api_subdir.rmdir()
        logger.info("Restructured API docs: api/algokit_subscriber/* -> api/*")

    # Remove the root index.md (Sphinx-generated, not needed for devportal)
    root_index = outdir / "index.md"
    if root_index.exists():
        root_index.unlink()
        logger.info("Removed root index.md")

    # Remove .doctrees directory (build artifacts)
    doctrees = outdir / ".doctrees"
    if doctrees.exists():
        shutil.rmtree(doctrees)
        logger.info("Removed .doctrees directory")


def add_frontmatter_to_files(app: Sphinx, exception: Exception | None) -> None:
    """Post-build hook to add frontmatter and restructure output."""
    # Only process for markdown builder
    if app.builder.name != "markdown":
        return

    # Don't process if build failed
    if exception:
        return

    outdir = Path(app.outdir)

    # First, add frontmatter to all markdown files
    md_files = list(outdir.rglob("*.md"))
    modified_count = 0

    for md_file in md_files:
        content = md_file.read_text(encoding="utf-8")

        # Skip if already has frontmatter
        if content.startswith("---\n"):
            continue

        # Extract title
        title = extract_title_from_content(content, md_file.stem)

        # Create frontmatter
        frontmatter = f"---\ntitle: {title}\n---\n\n"

        # Write back with frontmatter
        md_file.write_text(frontmatter + content, encoding="utf-8")
        modified_count += 1
        logger.info(f"Added frontmatter to: {md_file.relative_to(outdir)}")

    logger.info(f"Frontmatter added to {modified_count} files")

    # Then restructure the output for devportal
    restructure_devportal_output(outdir)


def setup(app: Sphinx) -> dict:
    """Sphinx extension setup."""
    app.connect("build-finished", add_frontmatter_to_files)

    return {
        "version": "1.0.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
