---
title: algokit_subscriber.transform
---

# [`algokit_subscriber.transform`](#module-algokit_subscriber.transform)

## Module Contents

### Classes

| [`ExtractedBlockTransaction`](#algokit_subscriber.transform.ExtractedBlockTransaction)                 |    |
|--------------------------------------------------------------------------------------------------------|----|
| [`TransactionInBlockWithChildOffset`](#algokit_subscriber.transform.TransactionInBlockWithChildOffset) |    |

### Functions

| [`algod_on_complete_to_indexer_on_complete`](#algokit_subscriber.transform.algod_on_complete_to_indexer_on_complete)                 |                                                                                                                      |
|--------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| [`remove_nulls`](#algokit_subscriber.transform.remove_nulls)                                                                         |                                                                                                                      |
| [`get_transaction_from_block_payout`](#algokit_subscriber.transform.get_transaction_from_block_payout)                               | Gets the synthetic transaction for the block payout as defined in the indexer                                        |
| [`get_block_transactions`](#algokit_subscriber.transform.get_block_transactions)                                                     |                                                                                                                      |
| [`get_block_inner_transactions`](#algokit_subscriber.transform.get_block_inner_transactions)                                         |                                                                                                                      |
| [`extract_transaction_from_block_transaction`](#algokit_subscriber.transform.extract_transaction_from_block_transaction)             | Transform a raw block transaction representation into a `algosdk.Transaction` object and other key transaction data. |
| [`extract_and_normalise_transaction`](#algokit_subscriber.transform.extract_and_normalise_transaction)                               | Extract and normalize a transaction from a block transaction.                                                        |
| [`get_tx_id_from_block_transaction`](#algokit_subscriber.transform.get_tx_id_from_block_transaction)                                 | Get the transaction ID from a block transaction.                                                                     |
| [`convert_bytes_to_base64`](#algokit_subscriber.transform.convert_bytes_to_base64)                                                   | Recursively iterate over a nested dict and convert any bytes values to base64 strings.                               |
| [`get_indexer_transaction_from_algod_transaction`](#algokit_subscriber.transform.get_indexer_transaction_from_algod_transaction)     |                                                                                                                      |
| [`block_data_to_block_metadata`](#algokit_subscriber.transform.block_data_to_block_metadata)                                         | Extract key metadata from a block.                                                                                   |
| [`count_all_transactions`](#algokit_subscriber.transform.count_all_transactions)                                                     |                                                                                                                      |
| [`extract_balance_changes_from_block_transaction`](#algokit_subscriber.transform.extract_balance_changes_from_block_transaction)     |                                                                                                                      |
| [`extract_balance_changes_from_indexer_transaction`](#algokit_subscriber.transform.extract_balance_changes_from_indexer_transaction) |                                                                                                                      |

### Data

| [`ALGORAND_ZERO_ADDRESS`](#algokit_subscriber.transform.ALGORAND_ZERO_ADDRESS)   |    |
|----------------------------------------------------------------------------------|----|

### API

### ALGORAND_ZERO_ADDRESS

‘AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAY5HFKQ’

### algod_on_complete_to_indexer_on_complete(algod_oc: int) → [algokit_subscriber.types.transaction.IndexerOnComplete](algokit_subscriber.types.transaction.md#algokit_subscriber.types.transaction.IndexerOnComplete)

### remove_nulls(obj: dict) → dict

### get_transaction_from_block_payout(block: [algokit_subscriber.types.block.Block](algokit_subscriber.types.block.md#algokit_subscriber.types.block.Block), round_offset: int) → [algokit_subscriber.types.block.TransactionInBlock](algokit_subscriber.types.block.md#algokit_subscriber.types.block.TransactionInBlock)

Gets the synthetic transaction for the block payout as defined in the indexer

See https://github.com/algorand/indexer/blob/084577338ad4882f5797b3e1b30b84718ad40333/idb/postgres/internal/writer/write_txn.go?plain=1#L180-L202

### get_block_transactions(block: [algokit_subscriber.types.block.Block](algokit_subscriber.types.block.md#algokit_subscriber.types.block.Block)) → list[[algokit_subscriber.types.block.TransactionInBlock](algokit_subscriber.types.block.md#algokit_subscriber.types.block.TransactionInBlock)]

### get_block_inner_transactions(block_transaction: [algokit_subscriber.types.block.BlockInnerTransaction](algokit_subscriber.types.block.md#algokit_subscriber.types.block.BlockInnerTransaction), block: [algokit_subscriber.types.block.Block](algokit_subscriber.types.block.md#algokit_subscriber.types.block.Block), parent_transaction: [algokit_subscriber.types.block.BlockTransaction](algokit_subscriber.types.block.md#algokit_subscriber.types.block.BlockTransaction), parent_transaction_id: str, round_index: int, get_round_offset: collections.abc.Callable, get_parent_offset: collections.abc.Callable) → list[[algokit_subscriber.types.block.TransactionInBlock](algokit_subscriber.types.block.md#algokit_subscriber.types.block.TransactionInBlock)]

### *class* ExtractedBlockTransaction

Bases: `typing.TypedDict`

#### transaction *: algokit_subscriber.types.transaction.AnyTransaction*

None

#### created_asset_id *: int | None*

None

#### created_app_id *: int | None*

None

#### asset_close_amount *: int | None*

None

#### close_amount *: int | None*

None

#### logs *: list[str] | None*

None

#### \_\_contains_\_()

#### \_\_delattr_\_()

#### \_\_delitem_\_()

#### \_\_dir_\_()

#### \_\_eq_\_()

#### \_\_format_\_()

#### \_\_ge_\_()

#### \_\_getattribute_\_()

#### \_\_getitem_\_()

#### \_\_getstate_\_()

#### \_\_gt_\_()

#### \_\_ior_\_()

#### \_\_iter_\_()

#### \_\_le_\_()

#### \_\_len_\_()

#### \_\_lt_\_()

#### \_\_ne_\_()

#### \_\_new_\_()

#### \_\_or_\_()

#### \_\_reduce_\_()

#### \_\_reduce_ex_\_()

#### \_\_repr_\_()

#### \_\_reversed_\_()

#### \_\_ror_\_()

#### \_\_setattr_\_()

#### \_\_setitem_\_()

#### \_\_sizeof_\_()

#### \_\_str_\_()

#### \_\_subclasshook_\_()

#### clear()

#### copy()

#### get()

#### items()

#### keys()

#### pop()

#### popitem()

#### setdefault()

#### update()

#### values()

### extract_transaction_from_block_transaction(block_transaction: [algokit_subscriber.types.block.BlockInnerTransaction](algokit_subscriber.types.block.md#algokit_subscriber.types.block.BlockInnerTransaction), genesis_hash: bytes, genesis_id: str) → [algokit_subscriber.transform.ExtractedBlockTransaction](#algokit_subscriber.transform.ExtractedBlockTransaction)

Transform a raw block transaction representation into a `algosdk.Transaction` object and other key transaction data.

Note: Doesn’t currently support `keyreg` (Key Registration) or `stpf` (State Proof) transactions.

* **Parameters:**
  * **block_transaction** ([*BlockInnerTransaction*](algokit_subscriber.types.block.md#algokit_subscriber.types.block.BlockInnerTransaction)) – The raw transaction from a block
  * **genesis_hash** (*bytes*) – The genesis hash
  * **genesis_id** (*str*) – The genesis ID
* **Returns:**
  The `algosdk.Transaction` object along with key secondary information from the block.
* **Return type:**
  [ExtractedBlockTransaction](#algokit_subscriber.transform.ExtractedBlockTransaction)

### extract_and_normalise_transaction(block_transaction: [algokit_subscriber.types.block.BlockInnerTransaction](algokit_subscriber.types.block.md#algokit_subscriber.types.block.BlockInnerTransaction) | [algokit_subscriber.types.block.BlockTransaction](algokit_subscriber.types.block.md#algokit_subscriber.types.block.BlockTransaction), genesis_hash: bytes, genesis_id: str) → dict[str, Any]

Extract and normalize a transaction from a block transaction.

* **Parameters:**
  * **block_transaction** ([*BlockTransaction*](algokit_subscriber.types.block.md#algokit_subscriber.types.block.BlockTransaction)) – The raw transaction from a block
  * **genesis_hash** (*bytes*) – The genesis hash
  * **genesis_id** (*str*) – The genesis ID
* **Returns:**
  The normalized transaction
* **Return type:**
  dict[str, Any]

### get_tx_id_from_block_transaction(block_transaction: [algokit_subscriber.types.block.BlockTransaction](algokit_subscriber.types.block.md#algokit_subscriber.types.block.BlockTransaction) | [algokit_subscriber.types.block.BlockInnerTransaction](algokit_subscriber.types.block.md#algokit_subscriber.types.block.BlockInnerTransaction), genesis_hash: bytes, genesis_id: str) → str

Get the transaction ID from a block transaction.

* **Parameters:**
  * **block_transaction** ([*BlockTransaction*](algokit_subscriber.types.block.md#algokit_subscriber.types.block.BlockTransaction) *|* [*BlockInnerTransaction*](algokit_subscriber.types.block.md#algokit_subscriber.types.block.BlockInnerTransaction)) – The block transaction
  * **genesis_hash** (*bytes*) – The genesis hash
  * **genesis_id** (*str*) – The genesis ID
* **Returns:**
  The transaction ID
* **Return type:**
  str

### *class* TransactionInBlockWithChildOffset

Bases: [`algokit_subscriber.types.block.TransactionInBlock`](algokit_subscriber.types.block.md#algokit_subscriber.types.block.TransactionInBlock)

#### get_child_offset *: typing_extensions.NotRequired[collections.abc.Callable[[], int]]*

None

#### block_transaction *: [BlockTransaction](algokit_subscriber.types.block.md#algokit_subscriber.types.block.BlockTransaction) | [BlockInnerTransaction](algokit_subscriber.types.block.md#algokit_subscriber.types.block.BlockInnerTransaction)*

None

#### round_offset *: int*

None

#### round_index *: int*

None

#### parent_transaction_id *: typing_extensions.NotRequired[None | str]*

None

#### parent_offset *: typing_extensions.NotRequired[None | int]*

None

#### genesis_hash *: bytes*

None

#### genesis_id *: str*

None

#### round_number *: int*

None

#### round_timestamp *: int*

None

#### transaction *: algosdk.transaction.Transaction*

None

#### created_asset_id *: typing_extensions.NotRequired[None | int]*

None

#### created_app_id *: typing_extensions.NotRequired[None | int]*

None

#### asset_close_amount *: typing_extensions.NotRequired[None | int]*

None

#### close_amount *: typing_extensions.NotRequired[None | int]*

None

#### logs *: typing_extensions.NotRequired[None | list[str]]*

None

#### \_\_contains_\_()

#### \_\_delattr_\_()

#### \_\_delitem_\_()

#### \_\_dir_\_()

#### \_\_eq_\_()

#### \_\_format_\_()

#### \_\_ge_\_()

#### \_\_getattribute_\_()

#### \_\_getitem_\_()

#### \_\_getstate_\_()

#### \_\_gt_\_()

#### \_\_ior_\_()

#### \_\_iter_\_()

#### \_\_le_\_()

#### \_\_len_\_()

#### \_\_lt_\_()

#### \_\_ne_\_()

#### \_\_new_\_()

#### \_\_or_\_()

#### \_\_reduce_\_()

#### \_\_reduce_ex_\_()

#### \_\_repr_\_()

#### \_\_reversed_\_()

#### \_\_ror_\_()

#### \_\_setattr_\_()

#### \_\_setitem_\_()

#### \_\_sizeof_\_()

#### \_\_str_\_()

#### \_\_subclasshook_\_()

#### clear()

#### copy()

#### get()

#### items()

#### keys()

#### pop()

#### popitem()

#### setdefault()

#### update()

#### values()

### convert_bytes_to_base64(obj: Any) → Any

Recursively iterate over a nested dict and convert any bytes values to base64 strings.

* **Parameters:**
  **obj** (*Any*) – The object to convert (can be a dict, list, or any other type)
* **Returns:**
  The object with all bytes values converted to base64 strings
* **Return type:**
  Any

### get_indexer_transaction_from_algod_transaction(t: [algokit_subscriber.types.block.TransactionInBlock](algokit_subscriber.types.block.md#algokit_subscriber.types.block.TransactionInBlock) | [algokit_subscriber.transform.TransactionInBlockWithChildOffset](#algokit_subscriber.transform.TransactionInBlockWithChildOffset), filter_name: str | None = None) → [algokit_subscriber.types.subscription.SubscribedTransaction](algokit_subscriber.types.subscription.md#algokit_subscriber.types.subscription.SubscribedTransaction)

### block_data_to_block_metadata(block_data: [algokit_subscriber.types.block.BlockData](algokit_subscriber.types.block.md#algokit_subscriber.types.block.BlockData)) → [algokit_subscriber.types.subscription.BlockMetadata](algokit_subscriber.types.subscription.md#algokit_subscriber.types.subscription.BlockMetadata)

Extract key metadata from a block.

* **Parameters:**
  **block_data** ([*BlockData*](algokit_subscriber.types.block.md#algokit_subscriber.types.block.BlockData)) – The raw block data
* **Returns:**
  The block metadata
* **Return type:**
  [BlockMetadata](algokit_subscriber.types.subscription.md#algokit_subscriber.types.subscription.BlockMetadata)

### count_all_transactions(txns: collections.abc.Sequence[[algokit_subscriber.types.block.BlockTransaction](algokit_subscriber.types.block.md#algokit_subscriber.types.block.BlockTransaction) | [algokit_subscriber.types.block.BlockInnerTransaction](algokit_subscriber.types.block.md#algokit_subscriber.types.block.BlockInnerTransaction)]) → int

### extract_balance_changes_from_block_transaction(transaction: [algokit_subscriber.types.block.BlockTransaction](algokit_subscriber.types.block.md#algokit_subscriber.types.block.BlockTransaction) | [algokit_subscriber.types.block.BlockInnerTransaction](algokit_subscriber.types.block.md#algokit_subscriber.types.block.BlockInnerTransaction)) → list[[algokit_subscriber.types.subscription.BalanceChange](algokit_subscriber.types.subscription.md#algokit_subscriber.types.subscription.BalanceChange)]

### extract_balance_changes_from_indexer_transaction(transaction: algokit_subscriber.types.indexer.TransactionResult) → list[[algokit_subscriber.types.subscription.BalanceChange](algokit_subscriber.types.subscription.md#algokit_subscriber.types.subscription.BalanceChange)]
