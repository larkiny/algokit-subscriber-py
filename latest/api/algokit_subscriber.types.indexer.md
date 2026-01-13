---
title: algokit_subscriber.types.indexer
---

# [`algokit_subscriber.types.indexer`](#module-algokit_subscriber.types.indexer)

## Module Contents

### Classes

| [`StateProofParticipant`](#algokit_subscriber.types.indexer.StateProofParticipant)               |    |
|--------------------------------------------------------------------------------------------------|----|
| [`TransactionSignature`](#algokit_subscriber.types.indexer.TransactionSignature)                 |    |
| [`MultisigTransactionSignature`](#algokit_subscriber.types.indexer.MultisigTransactionSignature) |    |
| [`EvalDelta`](#algokit_subscriber.types.indexer.EvalDelta)                                       |    |
| [`ApplicationOnComplete`](#algokit_subscriber.types.indexer.ApplicationOnComplete)               |    |
| [`SignatureType`](#algokit_subscriber.types.indexer.SignatureType)                               |    |
| [`AccountStatus`](#algokit_subscriber.types.indexer.AccountStatus)                               |    |

### Data

| [`TealKeyValue`](#algokit_subscriber.types.indexer.TealKeyValue)                                         |    |
|----------------------------------------------------------------------------------------------------------|----|
| [`TransactionSearchResults`](#algokit_subscriber.types.indexer.TransactionSearchResults)                 |    |
| [`AccountLookupResult`](#algokit_subscriber.types.indexer.AccountLookupResult)                           |    |
| [`AssetsLookupResult`](#algokit_subscriber.types.indexer.AssetsLookupResult)                             |    |
| [`AssetsCreatedLookupResult`](#algokit_subscriber.types.indexer.AssetsCreatedLookupResult)               |    |
| [`ApplicationCreatedLookupResult`](#algokit_subscriber.types.indexer.ApplicationCreatedLookupResult)     |    |
| [`AssetLookupResult`](#algokit_subscriber.types.indexer.AssetLookupResult)                               |    |
| [`LookupAssetHoldingsOptions`](#algokit_subscriber.types.indexer.LookupAssetHoldingsOptions)             |    |
| [`AssetBalancesLookupResult`](#algokit_subscriber.types.indexer.AssetBalancesLookupResult)               |    |
| [`TransactionLookupResult`](#algokit_subscriber.types.indexer.TransactionLookupResult)                   |    |
| [`ApplicationLookupResult`](#algokit_subscriber.types.indexer.ApplicationLookupResult)                   |    |
| [`TransactionResult`](#algokit_subscriber.types.indexer.TransactionResult)                               |    |
| [`AccountResult`](#algokit_subscriber.types.indexer.AccountResult)                                       |    |
| [`PaymentTransactionResult`](#algokit_subscriber.types.indexer.PaymentTransactionResult)                 |    |
| [`StateProofTransactionResult`](#algokit_subscriber.types.indexer.StateProofTransactionResult)           |    |
| [`StateProofMessage`](#algokit_subscriber.types.indexer.StateProofMessage)                               |    |
| [`StateProof`](#algokit_subscriber.types.indexer.StateProof)                                             |    |
| [`StateProofReveal`](#algokit_subscriber.types.indexer.StateProofReveal)                                 |    |
| [`StateProofVerifier`](#algokit_subscriber.types.indexer.StateProofVerifier)                             |    |
| [`StateProofSigSlot`](#algokit_subscriber.types.indexer.StateProofSigSlot)                               |    |
| [`MerkleSignature`](#algokit_subscriber.types.indexer.MerkleSignature)                                   |    |
| [`MerkleArrayProof`](#algokit_subscriber.types.indexer.MerkleArrayProof)                                 |    |
| [`HashFactory`](#algokit_subscriber.types.indexer.HashFactory)                                           |    |
| [`ApplicationTransactionResult`](#algokit_subscriber.types.indexer.ApplicationTransactionResult)         |    |
| [`AssetConfigTransactionResult`](#algokit_subscriber.types.indexer.AssetConfigTransactionResult)         |    |
| [`AssetFreezeTransactionResult`](#algokit_subscriber.types.indexer.AssetFreezeTransactionResult)         |    |
| [`AssetTransferTransactionResult`](#algokit_subscriber.types.indexer.AssetTransferTransactionResult)     |    |
| [`KeyRegistrationTransactionResult`](#algokit_subscriber.types.indexer.KeyRegistrationTransactionResult) |    |
| [`AssetResult`](#algokit_subscriber.types.indexer.AssetResult)                                           |    |
| [`ApplicationResult`](#algokit_subscriber.types.indexer.ApplicationResult)                               |    |
| [`LogicTransactionSignature`](#algokit_subscriber.types.indexer.LogicTransactionSignature)               |    |
| [`MultisigTransactionSubSignature`](#algokit_subscriber.types.indexer.MultisigTransactionSubSignature)   |    |
| [`ApplicationParams`](#algokit_subscriber.types.indexer.ApplicationParams)                               |    |
| [`StateSchema`](#algokit_subscriber.types.indexer.StateSchema)                                           |    |
| [`AssetParams`](#algokit_subscriber.types.indexer.AssetParams)                                           |    |
| [`AccountParticipation`](#algokit_subscriber.types.indexer.AccountParticipation)                         |    |
| [`AppLocalState`](#algokit_subscriber.types.indexer.AppLocalState)                                       |    |
| [`AssetHolding`](#algokit_subscriber.types.indexer.AssetHolding)                                         |    |
| [`MiniAssetHolding`](#algokit_subscriber.types.indexer.MiniAssetHolding)                                 |    |

### API

### TealKeyValue

None

### TransactionSearchResults

‘TypedDict(…)’

### AccountLookupResult

‘TypedDict(…)’

### AssetsLookupResult

‘TypedDict(…)’

### AssetsCreatedLookupResult

‘TypedDict(…)’

### ApplicationCreatedLookupResult

‘TypedDict(…)’

### AssetLookupResult

‘TypedDict(…)’

### LookupAssetHoldingsOptions

‘TypedDict(…)’

### AssetBalancesLookupResult

‘TypedDict(…)’

### TransactionLookupResult

‘TypedDict(…)’

### ApplicationLookupResult

‘TypedDict(…)’

### TransactionResult

‘TypedDict(…)’

### AccountResult

‘TypedDict(…)’

### PaymentTransactionResult

‘TypedDict(…)’

### StateProofTransactionResult

‘TypedDict(…)’

### StateProofMessage

‘TypedDict(…)’

### StateProof

‘TypedDict(…)’

### StateProofReveal

‘TypedDict(…)’

### *class* StateProofParticipant

Bases: `typing.TypedDict`

#### verifier *: StateProofVerifier*

None

#### weight *: int*

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

### StateProofVerifier

‘TypedDict(…)’

### StateProofSigSlot

‘TypedDict(…)’

### MerkleSignature

‘TypedDict(…)’

### MerkleArrayProof

‘TypedDict(…)’

### HashFactory

‘TypedDict(…)’

### ApplicationTransactionResult

‘TypedDict(…)’

### AssetConfigTransactionResult

‘TypedDict(…)’

### AssetFreezeTransactionResult

‘TypedDict(…)’

### AssetTransferTransactionResult

‘TypedDict(…)’

### KeyRegistrationTransactionResult

‘TypedDict(…)’

### AssetResult

‘TypedDict(…)’

### ApplicationResult

‘TypedDict(…)’

### *class* TransactionSignature

Bases: `typing.TypedDict`

#### logicsig *: typing_extensions.NotRequired[LogicTransactionSignature]*

None

#### multisig *: typing_extensions.NotRequired[[MultisigTransactionSignature](#algokit_subscriber.types.indexer.MultisigTransactionSignature)]*

None

#### sig *: typing_extensions.NotRequired[str]*

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

### LogicTransactionSignature

‘TypedDict(…)’

### *class* MultisigTransactionSignature

Bases: `typing.TypedDict`

#### subsignature *: list[MultisigTransactionSubSignature]*

None

#### threshold *: int*

None

#### version *: int*

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

### MultisigTransactionSubSignature

‘TypedDict(…)’

### *class* EvalDelta

Bases: `typing.TypedDict`

#### action *: int*

None

#### bytes *: typing_extensions.NotRequired[str]*

None

#### uint *: typing_extensions.NotRequired[int]*

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

### ApplicationParams

‘TypedDict(…)’

### StateSchema

‘TypedDict(…)’

### *class* ApplicationOnComplete(\*args, \*\*kwds)

Bases: `enum.Enum`

#### noop

‘noop’

#### optin

‘optin’

#### closeout

‘closeout’

#### clear

‘clear’

#### update

‘update’

#### delete

‘delete’

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

### AssetParams

‘TypedDict(…)’

### *class* SignatureType(\*args, \*\*kwds)

Bases: `enum.Enum`

#### sig

‘sig’

#### msig

‘msig’

#### lsig

‘lsig’

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

### *class* AccountStatus(\*args, \*\*kwds)

Bases: `enum.Enum`

#### Offline

‘Offline’

#### Online

‘Online’

#### NotParticipating

‘NotParticipating’

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

### AccountParticipation

‘TypedDict(…)’

### AppLocalState

‘TypedDict(…)’

### AssetHolding

‘TypedDict(…)’

### MiniAssetHolding

‘TypedDict(…)’
