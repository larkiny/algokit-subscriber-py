---
title: algokit_subscriber.types.subscription
---

# [`algokit_subscriber.types.subscription`](#module-algokit_subscriber.types.subscription)

## Module Contents

### Classes

| [`BalanceChangeRole`](#algokit_subscriber.types.subscription.BalanceChangeRole)                                 |                                                                                     |
|-----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| [`TransactionSubscriptionResult`](#algokit_subscriber.types.subscription.TransactionSubscriptionResult)         | The result of a single subscription pull/poll.                                      |
| [`BlockMetadata`](#algokit_subscriber.types.subscription.BlockMetadata)                                         | Metadata about a block that was retrieved from algod.                               |
| [`BlockRewards`](#algokit_subscriber.types.subscription.BlockRewards)                                           |                                                                                     |
| [`BlockUpgradeState`](#algokit_subscriber.types.subscription.BlockUpgradeState)                                 |                                                                                     |
| [`SubscribedTransaction`](#algokit_subscriber.types.subscription.SubscribedTransaction)                         | The common model used to expose a transaction that is returned from a subscription. |
| [`BalanceChange`](#algokit_subscriber.types.subscription.BalanceChange)                                         | Represents a balance change effect for a transaction.                               |
| [`BeforePollMetadata`](#algokit_subscriber.types.subscription.BeforePollMetadata)                               | Metadata about an impending subscription poll.                                      |
| [`TransactionFilter`](#algokit_subscriber.types.subscription.TransactionFilter)                                 |                                                                                     |
| [`NamedTransactionFilter`](#algokit_subscriber.types.subscription.NamedTransactionFilter)                       | Specify a named filter to apply to find transactions of interest.                   |
| [`CoreTransactionSubscriptionParams`](#algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams) |                                                                                     |
| [`TransactionSubscriptionParams`](#algokit_subscriber.types.subscription.TransactionSubscriptionParams)         |                                                                                     |
| [`WatermarkPersistence`](#algokit_subscriber.types.subscription.WatermarkPersistence)                           |                                                                                     |
| [`AlgorandSubscriberConfig`](#algokit_subscriber.types.subscription.AlgorandSubscriberConfig)                   | Configuration for the subscriber.                                                   |
| [`SubscriberConfigFilter`](#algokit_subscriber.types.subscription.SubscriberConfigFilter)                       | A single event to subscribe to / emit.                                              |

### API

### *class* BalanceChangeRole(\*args, \*\*kwds)

Bases: `enum.Enum`

#### Sender

‘Sender’

#### Receiver

‘Receiver’

#### CloseTo

‘CloseTo’

#### AssetCreator

‘AssetCreator’

#### AssetDestroyer

‘AssetDestroyer’

#### *classmethod* \_\_signature_\_()

#### \_\_new_\_(value)

#### \_\_repr_\_()

#### \_\_str_\_()

#### \_\_dir_\_()

#### \_\_format_\_(format_spec)

#### \_\_hash_\_()

#### \_\_reduce_ex_\_(proto)

#### \_\_deepcopy_\_(memo)

#### \_\_copy_\_()

#### name()

#### value()

### *class* TransactionSubscriptionResult

Bases: `typing.TypedDict`

The result of a single subscription pull/poll.

### Initialization

Initialize self.  See help(type(self)) for accurate signature.

#### synced_round_range *: tuple[int, int]*

None

The round range that was synced from/to

#### current_round *: int*

None

The current detected tip of the configured Algorand blockchain.

#### starting_watermark *: int*

None

The watermark value that was retrieved at the start of the subscription poll.

#### new_watermark *: int*

None

The new watermark value to persist for the next call to
`get_subscribed_transactions` to continue the sync.
Will be equal to `synced_round_range[1]`. Only persist this
after processing (or in the same atomic transaction as)
subscribed transactions to keep it reliable.

#### subscribed_transactions *: list[[SubscribedTransaction](#algokit_subscriber.types.subscription.SubscribedTransaction)]*

None

Any transactions that matched the given filter within
the synced round range. This substantively uses the indexer transaction
format to represent the data with some additional fields.

#### block_metadata *: typing_extensions.NotRequired[list[[BlockMetadata](#algokit_subscriber.types.subscription.BlockMetadata)]]*

None

The metadata about any blocks that were retrieved from algod as part
of the subscription poll.

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

### *class* BlockMetadata

Bases: `typing.TypedDict`

Metadata about a block that was retrieved from algod.

### Initialization

Initialize self.  See help(type(self)) for accurate signature.

#### hash *: typing_extensions.NotRequired[str | None]*

None

The base64 block hash.

#### round *: int*

None

The round of the block.

#### timestamp *: int*

None

Block creation timestamp in seconds since epoch

#### genesis_id *: str*

None

The genesis ID of the chain.

#### genesis_hash *: str*

None

The base64 genesis hash of the chain.

#### previous_block_hash *: typing_extensions.NotRequired[str | None]*

None

The base64 previous block hash.

#### seed *: str*

None

The base64 seed of the block.

#### rewards *: typing_extensions.NotRequired[[BlockRewards](#algokit_subscriber.types.subscription.BlockRewards)]*

None

Fields relating to rewards

#### parent_transaction_count *: int*

None

Count of parent transactions in this block

#### full_transaction_count *: int*

None

Full count of transactions and inner transactions (recursively) in this block.

#### txn_counter *: int*

None

Number of the next transaction that will be committed after this block. It is 0 when no transactions have ever been committed (since TxnCounter started being supported).

#### transactions_root *: str*

None

Root of transaction merkle tree using SHA512_256 hash function.
This commitment is computed based on the PaysetCommit type specified in the block’s consensus protocol.

#### transactions_root_sha256 *: str*

None

TransactionsRootSHA256 is an auxiliary TransactionRoot, built using a vector commitment instead of a merkle tree, and SHA256 hash function instead of the default SHA512_256. This commitment can be used on environments where only the SHA256 function exists.

#### upgrade_state *: typing_extensions.NotRequired[[BlockUpgradeState](#algokit_subscriber.types.subscription.BlockUpgradeState)]*

None

Fields relating to a protocol upgrade.

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

### *class* BlockRewards

Bases: `typing.TypedDict`

#### fee_sink *: str*

None

FeeSink is an address that accepts transaction fees, it can only spend to the incentive pool.

#### rewards_calculation_round *: int*

None

number of leftover MicroAlgos after the distribution of rewards-rate MicroAlgos for every reward unit in the next round.

#### rewards_level *: int*

None

How many rewards, in MicroAlgos, have been distributed to each RewardUnit of MicroAlgos since genesis.

#### rewards_pool *: str*

None

RewardsPool is an address that accepts periodic injections from the fee-sink and continually redistributes them as rewards.

#### rewards_rate *: int*

None

Number of new MicroAlgos added to the participation stake from rewards at the next round.

#### rewards_residue *: int*

None

Number of leftover MicroAlgos after the distribution of RewardsRate/rewardUnits MicroAlgos for every reward unit in the next round.

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

### *class* BlockUpgradeState

Bases: `typing.TypedDict`

#### current_protocol *: str*

None

Current protocol version

#### next_protocol *: typing_extensions.NotRequired[None | str]*

None

The next proposed protocol version.

#### next_protocol_approvals *: typing_extensions.NotRequired[None | int]*

None

Number of blocks which approved the protocol upgrade.

#### next_protocol_vote_before *: typing_extensions.NotRequired[None | int]*

None

Deadline round for this protocol upgrade (No votes will be consider after this round).

#### next_protocol_switch_on *: typing_extensions.NotRequired[None | int]*

None

Round on which the protocol upgrade will take effect.

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

### *class* SubscribedTransaction

Bases: [`algokit_subscriber.types.indexer.TransactionResult`](algokit_subscriber.types.indexer.md#algokit_subscriber.types.indexer.TransactionResult)

The common model used to expose a transaction that is returned from a subscription.

Substantively, based on the Indexer `TransactionResult` model format with some modifications to:

* Add the `parent_transaction_id` field so inner transactions have a reference to their parent
* Override the type of `inner_txns` to be `SubscribedTransaction[]` so inner transactions (recursively) get these extra fields too
* Add emitted ARC-28 events via `arc28_events`
* Balance changes in algo or assets

### Initialization

Initialize self.  See help(type(self)) for accurate signature.

#### parent_transaction_id *: typing_extensions.NotRequired[None | str]*

None

The transaction ID of the parent of this transaction (if it’s an inner transaction).

#### inner_txns *: typing_extensions.NotRequired[list[[algokit_subscriber.types.subscription.SubscribedTransaction](#algokit_subscriber.types.subscription.SubscribedTransaction)]]*

None

Inner transactions produced by application execution.

#### arc28_events *: typing_extensions.NotRequired[list[[algokit_subscriber.types.arc28.EmittedArc28Event](algokit_subscriber.types.arc28.md#algokit_subscriber.types.arc28.EmittedArc28Event)]]*

None

Any ARC-28 events emitted from an app call.

#### filters_matched *: typing_extensions.NotRequired[list[str]]*

None

The names of any filters that matched the given transaction to result in it being ‘subscribed’.

#### balance_changes *: typing_extensions.NotRequired[list[[BalanceChange](#algokit_subscriber.types.subscription.BalanceChange)]]*

None

The balance changes in the transaction.

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

### *class* BalanceChange

Bases: `typing.TypedDict`

Represents a balance change effect for a transaction.

### Initialization

Initialize self.  See help(type(self)) for accurate signature.

#### address *: str*

None

The address that the balance change is for.

#### asset_id *: int*

None

The asset ID of the balance change, or 0 for Algos.

#### amount *: int*

None

The amount of the balance change in smallest divisible unit or microAlgos.

#### roles *: list[[algokit_subscriber.types.subscription.BalanceChangeRole](#algokit_subscriber.types.subscription.BalanceChangeRole)]*

None

The roles the account was playing that led to the balance change

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

### *class* BeforePollMetadata

Bases: `typing.TypedDict`

Metadata about an impending subscription poll.

### Initialization

Initialize self.  See help(type(self)) for accurate signature.

#### watermark *: int*

None

The current watermark of the subscriber

#### current_round *: int*

None

The current round of algod

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

### *class* TransactionFilter

Bases: `typing.TypedDict`

#### type *: typing_extensions.NotRequired[str | list[str]]*

None

Filter based on the given transaction type(s).

#### sender *: typing_extensions.NotRequired[str | list[str]]*

None

Filter to transactions sent from the specified address(es).

#### receiver *: typing_extensions.NotRequired[str | list[str]]*

None

Filter to transactions being received by the specified address(es).

#### note_prefix *: typing_extensions.NotRequired[str | bytes]*

None

Filter to transactions with a note having the given prefix.

#### app_id *: typing_extensions.NotRequired[int | list[int]]*

None

Filter to transactions against the app with the given ID(s).

#### app_create *: typing_extensions.NotRequired[bool]*

None

Filter to transactions that are creating an app.

#### app_on_complete *: typing_extensions.NotRequired[str | list[str]]*

None

Filter to transactions that have given on complete(s).

#### asset_id *: typing_extensions.NotRequired[int | list[int]]*

None

Filter to transactions against the asset with the given ID(s).

#### asset_create *: typing_extensions.NotRequired[bool]*

None

Filter to transactions that are creating an asset.

#### min_amount *: typing_extensions.NotRequired[int]*

None

Filter to transactions where the amount being transferred is greater
than or equal to the given minimum (microAlgos or decimal units of an ASA if type: axfer).

#### max_amount *: typing_extensions.NotRequired[int]*

None

Filter to transactions where the amount being transferred is less than
or equal to the given maximum (microAlgos or decimal units of an ASA if type: axfer).

#### method_signature *: typing_extensions.NotRequired[str | list[str]]*

None

Filter to app transactions that have the given ARC-0004 method selector(s) for
the given method signature as the first app argument.

#### app_call_arguments_match *: typing_extensions.NotRequired[collections.abc.Callable[[list[bytes] | None], bool]]*

None

Filter to app transactions that meet the given app arguments predicate.

#### arc28_events *: typing_extensions.NotRequired[list[dict[str, str]]]*

None

Filter to app transactions that emit the given ARC-28 events.
Note: the definitions for these events must be passed in to the subscription config via `arc28_events`.

#### balance_changes *: typing_extensions.NotRequired[list[dict[str, Union[int, list[int], str, list[str], [algokit_subscriber.types.subscription.BalanceChangeRole](#algokit_subscriber.types.subscription.BalanceChangeRole), list[[algokit_subscriber.types.subscription.BalanceChangeRole](#algokit_subscriber.types.subscription.BalanceChangeRole)]]]]]*

None

Filter to transactions that result in balance changes that match one or more of the given set of balance changes.

#### custom_filter *: typing_extensions.NotRequired[collections.abc.Callable[[algokit_subscriber.types.indexer.TransactionResult], bool]]*

None

Catch-all custom filter to filter for things that the rest of the filters don’t provide.

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

### *class* NamedTransactionFilter

Bases: `typing.TypedDict`

Specify a named filter to apply to find transactions of interest.

### Initialization

Initialize self.  See help(type(self)) for accurate signature.

#### name *: str*

None

The name to give the filter.

#### filter *: [algokit_subscriber.types.subscription.TransactionFilter](#algokit_subscriber.types.subscription.TransactionFilter)*

None

The filter itself.

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

### *class* CoreTransactionSubscriptionParams

Bases: `typing.TypedDict`

#### filters *: list[[algokit_subscriber.types.subscription.NamedTransactionFilter](#algokit_subscriber.types.subscription.NamedTransactionFilter)]*

None

The filter(s) to apply to find transactions of interest.

#### arc28_events *: typing_extensions.NotRequired[list[[algokit_subscriber.types.arc28.Arc28EventGroup](algokit_subscriber.types.arc28.md#algokit_subscriber.types.arc28.Arc28EventGroup)]]*

None

Any ARC-28 event definitions to process from app call logs

#### max_rounds_to_sync *: typing_extensions.NotRequired[int | None]*

None

The maximum number of rounds to sync from algod for each subscription pull/poll.
Defaults to 500.

#### max_indexer_rounds_to_sync *: typing_extensions.NotRequired[int | None]*

None

The maximum number of rounds to sync from indexer when using `sync_behaviour: 'catchup-with-indexer'`.

#### sync_behaviour *: Literal[catchup-with-algod, catchup-with-indexer, fail, skip-sync-newest, sync-oldest, sync-oldest-start-now]*

None

If the current tip of the configured Algorand blockchain is more than `max_rounds_to_sync`
past `watermark` then how should that be handled.

`fail`: Immediately fail
`skip-sync-newest`: Skip catchup and start syncing from the latest block regardless of the watermark.
`sync-oldest`: Start syncing from the watermark
`sync-oldest-start-now`: If the watermark is 0, start syncing from round 0. Otherwise skip to the latest block.
`catchup-with-indexer`: Use indexer to get missing transactions that match the filters starting from the watermark. Filters will be used in the indexer request to reduce the total amount of requests needed (relative to getting every block)

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

### *class* TransactionSubscriptionParams

Bases: [`algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams`](#algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams)

#### watermark *: int*

None

The current round watermark that transactions have previously been synced to.

#### current_round *: typing_extensions.NotRequired[int]*

None

The current tip of the configured Algorand blockchain.
If not provided, it will be resolved on demand.

#### filters *: list[[algokit_subscriber.types.subscription.NamedTransactionFilter](#algokit_subscriber.types.subscription.NamedTransactionFilter)]*

None

#### arc28_events *: typing_extensions.NotRequired[list[[algokit_subscriber.types.arc28.Arc28EventGroup](algokit_subscriber.types.arc28.md#algokit_subscriber.types.arc28.Arc28EventGroup)]]*

None

#### max_rounds_to_sync *: typing_extensions.NotRequired[int | None]*

None

#### max_indexer_rounds_to_sync *: typing_extensions.NotRequired[int | None]*

None

#### sync_behaviour *: Literal[catchup-with-algod, catchup-with-indexer, fail, skip-sync-newest, sync-oldest, sync-oldest-start-now]*

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

### *class* WatermarkPersistence

Bases: `typing.TypedDict`

#### get *: collections.abc.Callable[[], int | None]*

None

Method to retrieve the current watermark

#### set *: collections.abc.Callable[[int], None]*

None

Method to persist the new watermark

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

#### items()

#### keys()

#### pop()

#### popitem()

#### setdefault()

#### update()

#### values()

### *class* AlgorandSubscriberConfig

Bases: [`algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams`](#algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams)

Configuration for the subscriber.

### Initialization

Initialize self.  See help(type(self)) for accurate signature.

#### filters *: list[[SubscriberConfigFilter](#algokit_subscriber.types.subscription.SubscriberConfigFilter)]*

None

The set of filters to subscribe to / emit events for, along with optional data mappers.

#### frequency_in_seconds *: typing_extensions.NotRequired[int]*

None

The frequency to poll for new blocks in seconds; defaults to 1s

#### wait_for_block_when_at_tip *: typing_extensions.NotRequired[bool]*

None

Whether to wait via algod `/status/wait-for-block-after` endpoint when at the tip of the chain; reduces latency of subscription

#### watermark_persistence *: [algokit_subscriber.types.subscription.WatermarkPersistence](#algokit_subscriber.types.subscription.WatermarkPersistence)*

None

Methods to retrieve and persist the current watermark so syncing is resilient and maintains
its position in the chain

#### arc28_events *: typing_extensions.NotRequired[list[[algokit_subscriber.types.arc28.Arc28EventGroup](algokit_subscriber.types.arc28.md#algokit_subscriber.types.arc28.Arc28EventGroup)]]*

None

#### max_rounds_to_sync *: typing_extensions.NotRequired[int | None]*

None

#### max_indexer_rounds_to_sync *: typing_extensions.NotRequired[int | None]*

None

#### sync_behaviour *: Literal[catchup-with-algod, catchup-with-indexer, fail, skip-sync-newest, sync-oldest, sync-oldest-start-now]*

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

### *class* SubscriberConfigFilter

Bases: [`algokit_subscriber.types.subscription.NamedTransactionFilter`](#algokit_subscriber.types.subscription.NamedTransactionFilter)

A single event to subscribe to / emit.

### Initialization

Initialize self.  See help(type(self)) for accurate signature.

#### mapper *: typing_extensions.NotRequired[collections.abc.Callable[[list[[algokit_subscriber.types.subscription.SubscribedTransaction](#algokit_subscriber.types.subscription.SubscribedTransaction)]], list[Any]]]*

None

An optional data mapper if you want the event data to take a certain shape when subscribing to events with this filter name.

#### name *: str*

None

#### filter *: [algokit_subscriber.types.subscription.TransactionFilter](#algokit_subscriber.types.subscription.TransactionFilter)*

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
