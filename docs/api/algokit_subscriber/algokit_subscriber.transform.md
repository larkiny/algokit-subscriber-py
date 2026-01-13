# {py:mod}`algokit_subscriber.transform`

```{py:module} algokit_subscriber.transform
```

```{autodoc2-docstring} algokit_subscriber.transform
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ExtractedBlockTransaction <algokit_subscriber.transform.ExtractedBlockTransaction>`
  -
* - {py:obj}`TransactionInBlockWithChildOffset <algokit_subscriber.transform.TransactionInBlockWithChildOffset>`
  - ```{autodoc2-docstring} algokit_subscriber.transform.TransactionInBlockWithChildOffset
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`algod_on_complete_to_indexer_on_complete <algokit_subscriber.transform.algod_on_complete_to_indexer_on_complete>`
  - ```{autodoc2-docstring} algokit_subscriber.transform.algod_on_complete_to_indexer_on_complete
    :summary:
    ```
* - {py:obj}`remove_nulls <algokit_subscriber.transform.remove_nulls>`
  - ```{autodoc2-docstring} algokit_subscriber.transform.remove_nulls
    :summary:
    ```
* - {py:obj}`get_transaction_from_block_payout <algokit_subscriber.transform.get_transaction_from_block_payout>`
  - ```{autodoc2-docstring} algokit_subscriber.transform.get_transaction_from_block_payout
    :summary:
    ```
* - {py:obj}`get_block_transactions <algokit_subscriber.transform.get_block_transactions>`
  - ```{autodoc2-docstring} algokit_subscriber.transform.get_block_transactions
    :summary:
    ```
* - {py:obj}`get_block_inner_transactions <algokit_subscriber.transform.get_block_inner_transactions>`
  - ```{autodoc2-docstring} algokit_subscriber.transform.get_block_inner_transactions
    :summary:
    ```
* - {py:obj}`extract_transaction_from_block_transaction <algokit_subscriber.transform.extract_transaction_from_block_transaction>`
  - ```{autodoc2-docstring} algokit_subscriber.transform.extract_transaction_from_block_transaction
    :summary:
    ```
* - {py:obj}`extract_and_normalise_transaction <algokit_subscriber.transform.extract_and_normalise_transaction>`
  - ```{autodoc2-docstring} algokit_subscriber.transform.extract_and_normalise_transaction
    :summary:
    ```
* - {py:obj}`get_tx_id_from_block_transaction <algokit_subscriber.transform.get_tx_id_from_block_transaction>`
  - ```{autodoc2-docstring} algokit_subscriber.transform.get_tx_id_from_block_transaction
    :summary:
    ```
* - {py:obj}`convert_bytes_to_base64 <algokit_subscriber.transform.convert_bytes_to_base64>`
  - ```{autodoc2-docstring} algokit_subscriber.transform.convert_bytes_to_base64
    :summary:
    ```
* - {py:obj}`get_indexer_transaction_from_algod_transaction <algokit_subscriber.transform.get_indexer_transaction_from_algod_transaction>`
  - ```{autodoc2-docstring} algokit_subscriber.transform.get_indexer_transaction_from_algod_transaction
    :summary:
    ```
* - {py:obj}`block_data_to_block_metadata <algokit_subscriber.transform.block_data_to_block_metadata>`
  - ```{autodoc2-docstring} algokit_subscriber.transform.block_data_to_block_metadata
    :summary:
    ```
* - {py:obj}`count_all_transactions <algokit_subscriber.transform.count_all_transactions>`
  - ```{autodoc2-docstring} algokit_subscriber.transform.count_all_transactions
    :summary:
    ```
* - {py:obj}`extract_balance_changes_from_block_transaction <algokit_subscriber.transform.extract_balance_changes_from_block_transaction>`
  - ```{autodoc2-docstring} algokit_subscriber.transform.extract_balance_changes_from_block_transaction
    :summary:
    ```
* - {py:obj}`extract_balance_changes_from_indexer_transaction <algokit_subscriber.transform.extract_balance_changes_from_indexer_transaction>`
  - ```{autodoc2-docstring} algokit_subscriber.transform.extract_balance_changes_from_indexer_transaction
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ALGORAND_ZERO_ADDRESS <algokit_subscriber.transform.ALGORAND_ZERO_ADDRESS>`
  - ```{autodoc2-docstring} algokit_subscriber.transform.ALGORAND_ZERO_ADDRESS
    :summary:
    ```
````

### API

````{py:data} ALGORAND_ZERO_ADDRESS
:canonical: algokit_subscriber.transform.ALGORAND_ZERO_ADDRESS
:value: >
   'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAY5HFKQ'

```{autodoc2-docstring} algokit_subscriber.transform.ALGORAND_ZERO_ADDRESS
```

````

````{py:function} algod_on_complete_to_indexer_on_complete(algod_oc: int) -> algokit_subscriber.types.transaction.IndexerOnComplete
:canonical: algokit_subscriber.transform.algod_on_complete_to_indexer_on_complete

```{autodoc2-docstring} algokit_subscriber.transform.algod_on_complete_to_indexer_on_complete
```
````

````{py:function} remove_nulls(obj: dict) -> dict
:canonical: algokit_subscriber.transform.remove_nulls

```{autodoc2-docstring} algokit_subscriber.transform.remove_nulls
```
````

````{py:function} get_transaction_from_block_payout(block: algokit_subscriber.types.block.Block, round_offset: int) -> algokit_subscriber.types.block.TransactionInBlock
:canonical: algokit_subscriber.transform.get_transaction_from_block_payout

```{autodoc2-docstring} algokit_subscriber.transform.get_transaction_from_block_payout
```
````

````{py:function} get_block_transactions(block: algokit_subscriber.types.block.Block) -> list[algokit_subscriber.types.block.TransactionInBlock]
:canonical: algokit_subscriber.transform.get_block_transactions

```{autodoc2-docstring} algokit_subscriber.transform.get_block_transactions
```
````

````{py:function} get_block_inner_transactions(block_transaction: algokit_subscriber.types.block.BlockInnerTransaction, block: algokit_subscriber.types.block.Block, parent_transaction: algokit_subscriber.types.block.BlockTransaction, parent_transaction_id: str, round_index: int, get_round_offset: collections.abc.Callable, get_parent_offset: collections.abc.Callable) -> list[algokit_subscriber.types.block.TransactionInBlock]
:canonical: algokit_subscriber.transform.get_block_inner_transactions

```{autodoc2-docstring} algokit_subscriber.transform.get_block_inner_transactions
```
````

`````{py:class} ExtractedBlockTransaction()
:canonical: algokit_subscriber.transform.ExtractedBlockTransaction

Bases: {py:obj}`typing.TypedDict`

````{py:attribute} transaction
:canonical: algokit_subscriber.transform.ExtractedBlockTransaction.transaction
:type: algokit_subscriber.types.transaction.AnyTransaction
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.transform.ExtractedBlockTransaction.transaction
```

````

````{py:attribute} created_asset_id
:canonical: algokit_subscriber.transform.ExtractedBlockTransaction.created_asset_id
:type: int | None
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.transform.ExtractedBlockTransaction.created_asset_id
```

````

````{py:attribute} created_app_id
:canonical: algokit_subscriber.transform.ExtractedBlockTransaction.created_app_id
:type: int | None
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.transform.ExtractedBlockTransaction.created_app_id
```

````

````{py:attribute} asset_close_amount
:canonical: algokit_subscriber.transform.ExtractedBlockTransaction.asset_close_amount
:type: int | None
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.transform.ExtractedBlockTransaction.asset_close_amount
```

````

````{py:attribute} close_amount
:canonical: algokit_subscriber.transform.ExtractedBlockTransaction.close_amount
:type: int | None
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.transform.ExtractedBlockTransaction.close_amount
```

````

````{py:attribute} logs
:canonical: algokit_subscriber.transform.ExtractedBlockTransaction.logs
:type: list[str] | None
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.transform.ExtractedBlockTransaction.logs
```

````

````{py:method} __contains__()
:canonical: algokit_subscriber.transform.ExtractedBlockTransaction.__contains__

````

````{py:method} __delattr__()
:canonical: algokit_subscriber.transform.ExtractedBlockTransaction.__delattr__

````

````{py:method} __delitem__()
:canonical: algokit_subscriber.transform.ExtractedBlockTransaction.__delitem__

````

````{py:method} __dir__()
:canonical: algokit_subscriber.transform.ExtractedBlockTransaction.__dir__

````

````{py:method} __eq__()
:canonical: algokit_subscriber.transform.ExtractedBlockTransaction.__eq__

````

````{py:method} __format__()
:canonical: algokit_subscriber.transform.ExtractedBlockTransaction.__format__

````

````{py:method} __ge__()
:canonical: algokit_subscriber.transform.ExtractedBlockTransaction.__ge__

````

````{py:method} __getattribute__()
:canonical: algokit_subscriber.transform.ExtractedBlockTransaction.__getattribute__

````

````{py:method} __getitem__()
:canonical: algokit_subscriber.transform.ExtractedBlockTransaction.__getitem__

````

````{py:method} __getstate__()
:canonical: algokit_subscriber.transform.ExtractedBlockTransaction.__getstate__

````

````{py:method} __gt__()
:canonical: algokit_subscriber.transform.ExtractedBlockTransaction.__gt__

````

````{py:method} __ior__()
:canonical: algokit_subscriber.transform.ExtractedBlockTransaction.__ior__

````

````{py:method} __iter__()
:canonical: algokit_subscriber.transform.ExtractedBlockTransaction.__iter__

````

````{py:method} __le__()
:canonical: algokit_subscriber.transform.ExtractedBlockTransaction.__le__

````

````{py:method} __len__()
:canonical: algokit_subscriber.transform.ExtractedBlockTransaction.__len__

````

````{py:method} __lt__()
:canonical: algokit_subscriber.transform.ExtractedBlockTransaction.__lt__

````

````{py:method} __ne__()
:canonical: algokit_subscriber.transform.ExtractedBlockTransaction.__ne__

````

````{py:method} __new__()
:canonical: algokit_subscriber.transform.ExtractedBlockTransaction.__new__

````

````{py:method} __or__()
:canonical: algokit_subscriber.transform.ExtractedBlockTransaction.__or__

````

````{py:method} __reduce__()
:canonical: algokit_subscriber.transform.ExtractedBlockTransaction.__reduce__

````

````{py:method} __reduce_ex__()
:canonical: algokit_subscriber.transform.ExtractedBlockTransaction.__reduce_ex__

````

````{py:method} __repr__()
:canonical: algokit_subscriber.transform.ExtractedBlockTransaction.__repr__

````

````{py:method} __reversed__()
:canonical: algokit_subscriber.transform.ExtractedBlockTransaction.__reversed__

````

````{py:method} __ror__()
:canonical: algokit_subscriber.transform.ExtractedBlockTransaction.__ror__

````

````{py:method} __setattr__()
:canonical: algokit_subscriber.transform.ExtractedBlockTransaction.__setattr__

````

````{py:method} __setitem__()
:canonical: algokit_subscriber.transform.ExtractedBlockTransaction.__setitem__

````

````{py:method} __sizeof__()
:canonical: algokit_subscriber.transform.ExtractedBlockTransaction.__sizeof__

````

````{py:method} __str__()
:canonical: algokit_subscriber.transform.ExtractedBlockTransaction.__str__

````

````{py:method} __subclasshook__()
:canonical: algokit_subscriber.transform.ExtractedBlockTransaction.__subclasshook__

````

````{py:method} clear()
:canonical: algokit_subscriber.transform.ExtractedBlockTransaction.clear

````

````{py:method} copy()
:canonical: algokit_subscriber.transform.ExtractedBlockTransaction.copy

````

````{py:method} get()
:canonical: algokit_subscriber.transform.ExtractedBlockTransaction.get

````

````{py:method} items()
:canonical: algokit_subscriber.transform.ExtractedBlockTransaction.items

````

````{py:method} keys()
:canonical: algokit_subscriber.transform.ExtractedBlockTransaction.keys

````

````{py:method} pop()
:canonical: algokit_subscriber.transform.ExtractedBlockTransaction.pop

````

````{py:method} popitem()
:canonical: algokit_subscriber.transform.ExtractedBlockTransaction.popitem

````

````{py:method} setdefault()
:canonical: algokit_subscriber.transform.ExtractedBlockTransaction.setdefault

````

````{py:method} update()
:canonical: algokit_subscriber.transform.ExtractedBlockTransaction.update

````

````{py:method} values()
:canonical: algokit_subscriber.transform.ExtractedBlockTransaction.values

````

`````

````{py:function} extract_transaction_from_block_transaction(block_transaction: algokit_subscriber.types.block.BlockInnerTransaction, genesis_hash: bytes, genesis_id: str) -> algokit_subscriber.transform.ExtractedBlockTransaction
:canonical: algokit_subscriber.transform.extract_transaction_from_block_transaction

```{autodoc2-docstring} algokit_subscriber.transform.extract_transaction_from_block_transaction
```
````

````{py:function} extract_and_normalise_transaction(block_transaction: algokit_subscriber.types.block.BlockInnerTransaction | algokit_subscriber.types.block.BlockTransaction, genesis_hash: bytes, genesis_id: str) -> dict[str, typing.Any]
:canonical: algokit_subscriber.transform.extract_and_normalise_transaction

```{autodoc2-docstring} algokit_subscriber.transform.extract_and_normalise_transaction
```
````

````{py:function} get_tx_id_from_block_transaction(block_transaction: algokit_subscriber.types.block.BlockTransaction | algokit_subscriber.types.block.BlockInnerTransaction, genesis_hash: bytes, genesis_id: str) -> str
:canonical: algokit_subscriber.transform.get_tx_id_from_block_transaction

```{autodoc2-docstring} algokit_subscriber.transform.get_tx_id_from_block_transaction
```
````

`````{py:class} TransactionInBlockWithChildOffset
:canonical: algokit_subscriber.transform.TransactionInBlockWithChildOffset

Bases: {py:obj}`algokit_subscriber.types.block.TransactionInBlock`

```{autodoc2-docstring} algokit_subscriber.transform.TransactionInBlockWithChildOffset
```

````{py:attribute} get_child_offset
:canonical: algokit_subscriber.transform.TransactionInBlockWithChildOffset.get_child_offset
:type: typing_extensions.NotRequired[collections.abc.Callable[[], int]]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.transform.TransactionInBlockWithChildOffset.get_child_offset
```

````

`````

````{py:function} convert_bytes_to_base64(obj: typing.Any) -> typing.Any
:canonical: algokit_subscriber.transform.convert_bytes_to_base64

```{autodoc2-docstring} algokit_subscriber.transform.convert_bytes_to_base64
```
````

````{py:function} get_indexer_transaction_from_algod_transaction(t: algokit_subscriber.types.block.TransactionInBlock | algokit_subscriber.transform.TransactionInBlockWithChildOffset, filter_name: str | None = None) -> algokit_subscriber.types.subscription.SubscribedTransaction
:canonical: algokit_subscriber.transform.get_indexer_transaction_from_algod_transaction

```{autodoc2-docstring} algokit_subscriber.transform.get_indexer_transaction_from_algod_transaction
```
````

````{py:function} block_data_to_block_metadata(block_data: algokit_subscriber.types.block.BlockData) -> algokit_subscriber.types.subscription.BlockMetadata
:canonical: algokit_subscriber.transform.block_data_to_block_metadata

```{autodoc2-docstring} algokit_subscriber.transform.block_data_to_block_metadata
```
````

````{py:function} count_all_transactions(txns: collections.abc.Sequence[algokit_subscriber.types.block.BlockTransaction | algokit_subscriber.types.block.BlockInnerTransaction]) -> int
:canonical: algokit_subscriber.transform.count_all_transactions

```{autodoc2-docstring} algokit_subscriber.transform.count_all_transactions
```
````

````{py:function} extract_balance_changes_from_block_transaction(transaction: algokit_subscriber.types.block.BlockTransaction | algokit_subscriber.types.block.BlockInnerTransaction) -> list[algokit_subscriber.types.subscription.BalanceChange]
:canonical: algokit_subscriber.transform.extract_balance_changes_from_block_transaction

```{autodoc2-docstring} algokit_subscriber.transform.extract_balance_changes_from_block_transaction
```
````

````{py:function} extract_balance_changes_from_indexer_transaction(transaction: algokit_subscriber.types.indexer.TransactionResult) -> list[algokit_subscriber.types.subscription.BalanceChange]
:canonical: algokit_subscriber.transform.extract_balance_changes_from_indexer_transaction

```{autodoc2-docstring} algokit_subscriber.transform.extract_balance_changes_from_indexer_transaction
```
````
