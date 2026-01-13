# {py:mod}`algokit_subscriber.utils`

```{py:module} algokit_subscriber.utils
```

```{autodoc2-docstring} algokit_subscriber.utils
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`range_inclusive <algokit_subscriber.utils.range_inclusive>`
  - ```{autodoc2-docstring} algokit_subscriber.utils.range_inclusive
    :summary:
    ```
* - {py:obj}`chunk_array <algokit_subscriber.utils.chunk_array>`
  - ```{autodoc2-docstring} algokit_subscriber.utils.chunk_array
    :summary:
    ```
* - {py:obj}`reduce <algokit_subscriber.utils.reduce>`
  - ```{autodoc2-docstring} algokit_subscriber.utils.reduce
    :summary:
    ```
* - {py:obj}`encode_address <algokit_subscriber.utils.encode_address>`
  - ```{autodoc2-docstring} algokit_subscriber.utils.encode_address
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`logger <algokit_subscriber.utils.logger>`
  - ```{autodoc2-docstring} algokit_subscriber.utils.logger
    :summary:
    ```
````

### API

````{py:data} logger
:canonical: algokit_subscriber.utils.logger
:value: >
   'getLogger(...)'

```{autodoc2-docstring} algokit_subscriber.utils.logger
```

````

````{py:function} range_inclusive(start: int, end: int) -> list[int]
:canonical: algokit_subscriber.utils.range_inclusive

```{autodoc2-docstring} algokit_subscriber.utils.range_inclusive
```
````

````{py:function} chunk_array(arr: list[algokit_subscriber.utils.chunk_array.T], size: int) -> list[list[algokit_subscriber.utils.chunk_array.T]]
:canonical: algokit_subscriber.utils.chunk_array

```{autodoc2-docstring} algokit_subscriber.utils.chunk_array
```
````

````{py:function} reduce(array: list[algokit_subscriber.utils.reduce.T], callback: collections.abc.Callable[[algokit_subscriber.utils.reduce.T, algokit_subscriber.utils.reduce.T], algokit_subscriber.utils.reduce.T]) -> algokit_subscriber.utils.reduce.T
:canonical: algokit_subscriber.utils.reduce

```{autodoc2-docstring} algokit_subscriber.utils.reduce
```
````

````{py:function} encode_address(b: bytes) -> str
:canonical: algokit_subscriber.utils.encode_address

```{autodoc2-docstring} algokit_subscriber.utils.encode_address
```
````
