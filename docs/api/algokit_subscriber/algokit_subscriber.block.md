# {py:mod}`algokit_subscriber.block`

```{py:module} algokit_subscriber.block
```

```{autodoc2-docstring} algokit_subscriber.block
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`block_response_to_block_data <algokit_subscriber.block.block_response_to_block_data>`
  - ```{autodoc2-docstring} algokit_subscriber.block.block_response_to_block_data
    :summary:
    ```
* - {py:obj}`get_blocks_bulk <algokit_subscriber.block.get_blocks_bulk>`
  - ```{autodoc2-docstring} algokit_subscriber.block.get_blocks_bulk
    :summary:
    ```
````

### API

````{py:function} block_response_to_block_data(response: bytes) -> algokit_subscriber.types.block.BlockData
:canonical: algokit_subscriber.block.block_response_to_block_data

```{autodoc2-docstring} algokit_subscriber.block.block_response_to_block_data
```
````

````{py:function} get_blocks_bulk(context: dict[str, int], client: algosdk.v2client.algod.AlgodClient) -> list[algokit_subscriber.types.block.BlockData]
:canonical: algokit_subscriber.block.get_blocks_bulk

```{autodoc2-docstring} algokit_subscriber.block.get_blocks_bulk
```
````
