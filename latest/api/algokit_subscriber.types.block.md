---
title: algokit_subscriber.types.block
---

# [`algokit_subscriber.types.block`](#module-algokit_subscriber.types.block)

## Module Contents

### Classes

| [`BlockValueDelta`](#algokit_subscriber.types.block.BlockValueDelta)                     | A value delta as a result of a block transaction                                                                                          |
|------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| [`BlockTransactionEvalDelta`](#algokit_subscriber.types.block.BlockTransactionEvalDelta) | Eval deltas for a block                                                                                                                   |
| [`TransactionInBlock`](#algokit_subscriber.types.block.TransactionInBlock)               | The representation of all important data for a single transaction or inner transaction<br/>and its side effects within a committed block. |
| [`BlockInnerTransaction`](#algokit_subscriber.types.block.BlockInnerTransaction)         |                                                                                                                                           |
| [`BlockTransaction`](#algokit_subscriber.types.block.BlockTransaction)                   | Data that is returned in a raw Algorand block for a single transaction                                                                    |
| [`Block`](#algokit_subscriber.types.block.Block)                                         | Data that is returned in a raw Algorand block.                                                                                            |
| [`BlockData`](#algokit_subscriber.types.block.BlockData)                                 | Data that is returned in a raw Algorand block.                                                                                            |

### Data

| [`LogicSig`](#algokit_subscriber.types.block.LogicSig)                                   |    |
|------------------------------------------------------------------------------------------|----|
| [`MultisigSig`](#algokit_subscriber.types.block.MultisigSig)                             |    |
| [`BlockAgreementCertificate`](#algokit_subscriber.types.block.BlockAgreementCertificate) |    |

### API

### *class* BlockValueDelta

Bases: `typing.TypedDict`

A value delta as a result of a block transaction

### Initialization

Initialize self.  See help(type(self)) for accurate signature.

#### action_type *: int*

None

DeltaAction is an enum of actions that may be performed when applying a delta to a TEAL key/value store:

* `1`: SetBytesAction indicates that a TEAL byte slice should be stored at a key
* `2`: SetUintAction indicates that a Uint should be stored at a key
* `3`: DeleteAction indicates that the value for a particular key should be deleted

#### bytes_value *: typing_extensions.NotRequired[bytes]*

None

Bytes value

#### uint_value *: typing_extensions.NotRequired[int]*

None

Uint64 value

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

### *class* BlockTransactionEvalDelta

Bases: `typing.TypedDict`

Eval deltas for a block

### Initialization

Initialize self.  See help(type(self)) for accurate signature.

#### gd *: dict[str, [algokit_subscriber.types.block.BlockValueDelta](#algokit_subscriber.types.block.BlockValueDelta)]*

None

The delta of global state, keyed by key

#### ld *: dict[int, dict[str, [algokit_subscriber.types.block.BlockValueDelta](#algokit_subscriber.types.block.BlockValueDelta)]]*

None

The delta of local state keyed by account ID offset in [txn.Sender, …txn.Accounts] and then keyed by key

#### lg *: list[str]*

None

Logs

#### itx *: typing_extensions.NotRequired[list[[BlockInnerTransaction](#algokit_subscriber.types.block.BlockInnerTransaction)]]*

None

Inner transactions

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

### LogicSig

None

### MultisigSig

None

### *class* TransactionInBlock

Bases: `typing.TypedDict`

The representation of all important data for a single transaction or inner transaction
and its side effects within a committed block.

### Initialization

Initialize self.  See help(type(self)) for accurate signature.

#### block_transaction *: [BlockTransaction](#algokit_subscriber.types.block.BlockTransaction) | [BlockInnerTransaction](#algokit_subscriber.types.block.BlockInnerTransaction)*

None

The block data for the transaction

#### round_offset *: int*

None

The offset of the transaction within the round including inner transactions.

@example

- 0
- 1
- 2
- 3
- 4
- 5

#### round_index *: int*

None

The index within the block.txns array of this transaction or if it’s an inner transaction of it’s ultimate parent transaction.

@example

- 0
- 1
- 1
- 1
- 1
- 2

#### parent_transaction_id *: typing_extensions.NotRequired[None | str]*

None

The ID of the parent transaction if this is an inner transaction.

#### parent_offset *: typing_extensions.NotRequired[None | int]*

None

The offset within the parent transaction.

@example

- `None`
- `None`
- 0
- 1
- 2
- `None`

#### genesis_hash *: bytes*

None

The binary genesis hash of the network the transaction is within.

#### genesis_id *: str*

None

The string genesis ID of the network the transaction is within.

#### round_number *: int*

None

The round number of the block the transaction is within.

#### round_timestamp *: int*

None

The round unix timestamp of the block the transaction is within.

#### transaction *: algosdk.transaction.Transaction*

None

The transaction as an algosdk `Transaction` object.

#### created_asset_id *: typing_extensions.NotRequired[None | int]*

None

The asset ID if an asset was created from this transaction.

#### created_app_id *: typing_extensions.NotRequired[None | int]*

None

The app ID if an app was created from this transaction.

#### asset_close_amount *: typing_extensions.NotRequired[None | int]*

None

The asset close amount if the sender asset position was closed from this transaction.

#### close_amount *: typing_extensions.NotRequired[None | int]*

None

The ALGO close amount if the sender account was closed from this transaction.

#### logs *: typing_extensions.NotRequired[None | list[str]]*

None

Any logs that were issued as a result of this transaction.

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

### *class* BlockInnerTransaction

Bases: `typing.TypedDict`

#### txn *: dict[str, Any]*

None

The encoded transaction data

#### dt *: typing_extensions.NotRequired[None | [algokit_subscriber.types.block.BlockTransactionEvalDelta](#algokit_subscriber.types.block.BlockTransactionEvalDelta)]*

None

The eval deltas for the block

#### caid *: typing_extensions.NotRequired[None | int]*

None

Asset ID when an asset is created by the transaction

#### apid *: typing_extensions.NotRequired[None | int]*

None

App ID when an app is created by the transaction

#### aca *: typing_extensions.NotRequired[None | int]*

None

Asset closing amount in decimal units

#### ca *: typing_extensions.NotRequired[None | int]*

None

Algo closing amount in microAlgos

#### sig *: typing_extensions.NotRequired[None | bytes]*

None

Transaction ED25519 signature

#### lsig *: typing_extensions.NotRequired[None | algokit_subscriber.types.block.LogicSig]*

None

Logic signature

#### msig *: typing_extensions.NotRequired[None | algokit_subscriber.types.block.MultisigSig]*

None

Transaction multisig signature

#### sgnr *: typing_extensions.NotRequired[None | bytes]*

None

The signer, if signing with a different key than the Transaction type `from` property indicates

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

### *class* BlockTransaction

Bases: [`algokit_subscriber.types.block.BlockInnerTransaction`](#algokit_subscriber.types.block.BlockInnerTransaction)

Data that is returned in a raw Algorand block for a single transaction

@see https://github.com/algorand/go-algorand/blob/master/data/transactions/signedtxn.go#L32

### Initialization

Initialize self.  See help(type(self)) for accurate signature.

#### hgi *: typing_extensions.NotRequired[None | bool]*

None

Has genesis id

#### hgh *: typing_extensions.NotRequired[None | bool]*

None

Has genesis hash

#### txn *: dict[str, Any]*

None

#### dt *: typing_extensions.NotRequired[None | [algokit_subscriber.types.block.BlockTransactionEvalDelta](#algokit_subscriber.types.block.BlockTransactionEvalDelta)]*

None

#### caid *: typing_extensions.NotRequired[None | int]*

None

#### apid *: typing_extensions.NotRequired[None | int]*

None

#### aca *: typing_extensions.NotRequired[None | int]*

None

#### ca *: typing_extensions.NotRequired[None | int]*

None

#### sig *: typing_extensions.NotRequired[None | bytes]*

None

#### lsig *: typing_extensions.NotRequired[None | algokit_subscriber.types.block.LogicSig]*

None

#### msig *: typing_extensions.NotRequired[None | algokit_subscriber.types.block.MultisigSig]*

None

#### sgnr *: typing_extensions.NotRequired[None | bytes]*

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

### BlockAgreementCertificate

None

### *class* Block

Bases: `typing.TypedDict`

Data that is returned in a raw Algorand block.

@see https://github.com/algorand/go-algorand/blob/master/data/bookkeeping/block.go#L32

### Initialization

Initialize self.  See help(type(self)) for accurate signature.

#### earn *: int*

None

RewardsLevel specifies how many rewards, in MicroAlgos, have
been distributed to each config.Protocol.RewardUnit of MicroAlgos
since genesis.

#### fees *: bytes*

None

The FeeSink accepts transaction fees. It can only spend to the incentive pool.

#### frac *: int*

None

The number of leftover MicroAlgos after the distribution of RewardsRate/rewardUnits
MicroAlgos for every reward unit in the next round.

#### gen *: str*

None

Genesis ID to which this block belongs.

#### gh *: bytes*

None

Genesis hash to which this block belongs.

#### prev *: typing_extensions.NotRequired[None | bytes]*

None

The hash of the previous block

#### proto *: str*

None

UpgradeState tracks the protocol upgrade state machine; proto is the current protocol.

#### rate *: typing_extensions.NotRequired[None | int]*

None

The number of new MicroAlgos added to the participation stake from rewards at the next round.

#### rnd *: int*

None

Round number.

#### rwcalr *: int*

None

The round at which the RewardsRate will be recalculated.

#### rwd *: bytes*

None

The RewardsPool accepts periodic injections from the
FeeSink and continually redistributes them to addresses as rewards.

#### seed *: bytes*

None

Sortition seed

#### tc *: int*

None

TxnCounter is the number of the next transaction that will be
committed after this block. Genesis blocks can start at either
0 or 1000, depending on a consensus parameter (AppForbidLowResources).

#### ts *: int*

None

Round time (unix timestamp)

#### txn *: bytes*

None

Root of transaction merkle tree using SHA512_256 hash function.
This commitment is computed based on the PaysetCommit type specified in the block’s consensus protocol.

#### txn256 *: str*

None

Root of transaction vector commitment merkle tree using SHA256 hash function.

#### nextproto *: typing_extensions.NotRequired[None | str]*

None

The next proposed protocol version.

#### nextyes *: typing_extensions.NotRequired[None | int]*

None

Number of blocks which approved the protocol upgrade.

#### nextbefore *: typing_extensions.NotRequired[None | int]*

None

Deadline round for this protocol upgrade (No votes will be considered after this round).

#### nextswitch *: typing_extensions.NotRequired[None | int]*

None

Round on which the protocol upgrade will take effect.

#### txns *: typing_extensions.NotRequired[None | list[[algokit_subscriber.types.block.BlockTransaction](#algokit_subscriber.types.block.BlockTransaction)]]*

None

The transactions within the block.

#### prp *: typing_extensions.NotRequired[None | bytes]*

None

Proposer is the proposer of this block. Like the Seed, agreement adds
this after the block is assembled by the transaction pool, so that the same block can be prepared
for multiple participating accounts in the same node. Therefore, it can not be used
to influence block evaluation. Populated if proto.Payouts.Enabled

#### fc *: typing_extensions.NotRequired[None | int]*

None

FeesCollected is the sum of all fees paid by transactions in this
block. Populated if proto.Payouts.Enabled

#### bi *: typing_extensions.NotRequired[None | int]*

None

Bonus is the bonus incentive to be paid for proposing this block.  It
begins as a consensus parameter value, and decays periodically.

#### pp *: typing_extensions.NotRequired[None | int]*

None

ProposerPayout is the amount that is moved from the FeeSink to
the Proposer in this block.  It is basically the
bonus + the payouts percent of FeesCollected, but may be zero’d by
proposer ineligibility.

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

### *class* BlockData

Bases: `typing.TypedDict`

Data that is returned in a raw Algorand block.

### Initialization

Initialize self.  See help(type(self)) for accurate signature.

#### block *: [algokit_subscriber.types.block.Block](#algokit_subscriber.types.block.Block)*

None

The block itself.

#### cert *: algokit_subscriber.types.block.BlockAgreementCertificate*

None

cert (BlockAgreementCertificate): The block certification.

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
