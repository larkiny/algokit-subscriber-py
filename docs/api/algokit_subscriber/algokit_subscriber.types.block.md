# {py:mod}`algokit_subscriber.types.block`

```{py:module} algokit_subscriber.types.block
```

```{autodoc2-docstring} algokit_subscriber.types.block
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`BlockValueDelta <algokit_subscriber.types.block.BlockValueDelta>`
  - ```{autodoc2-docstring} algokit_subscriber.types.block.BlockValueDelta
    :summary:
    ```
* - {py:obj}`BlockTransactionEvalDelta <algokit_subscriber.types.block.BlockTransactionEvalDelta>`
  - ```{autodoc2-docstring} algokit_subscriber.types.block.BlockTransactionEvalDelta
    :summary:
    ```
* - {py:obj}`TransactionInBlock <algokit_subscriber.types.block.TransactionInBlock>`
  - ```{autodoc2-docstring} algokit_subscriber.types.block.TransactionInBlock
    :summary:
    ```
* - {py:obj}`BlockInnerTransaction <algokit_subscriber.types.block.BlockInnerTransaction>`
  -
* - {py:obj}`BlockTransaction <algokit_subscriber.types.block.BlockTransaction>`
  - ```{autodoc2-docstring} algokit_subscriber.types.block.BlockTransaction
    :summary:
    ```
* - {py:obj}`Block <algokit_subscriber.types.block.Block>`
  - ```{autodoc2-docstring} algokit_subscriber.types.block.Block
    :summary:
    ```
* - {py:obj}`BlockData <algokit_subscriber.types.block.BlockData>`
  - ```{autodoc2-docstring} algokit_subscriber.types.block.BlockData
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`LogicSig <algokit_subscriber.types.block.LogicSig>`
  - ```{autodoc2-docstring} algokit_subscriber.types.block.LogicSig
    :summary:
    ```
* - {py:obj}`MultisigSig <algokit_subscriber.types.block.MultisigSig>`
  - ```{autodoc2-docstring} algokit_subscriber.types.block.MultisigSig
    :summary:
    ```
* - {py:obj}`BlockAgreementCertificate <algokit_subscriber.types.block.BlockAgreementCertificate>`
  - ```{autodoc2-docstring} algokit_subscriber.types.block.BlockAgreementCertificate
    :summary:
    ```
````

### API

`````{py:class} BlockValueDelta()
:canonical: algokit_subscriber.types.block.BlockValueDelta

Bases: {py:obj}`typing.TypedDict`

```{autodoc2-docstring} algokit_subscriber.types.block.BlockValueDelta
```

```{rubric} Initialization
```

```{autodoc2-docstring} algokit_subscriber.types.block.BlockValueDelta.__init__
```

````{py:attribute} action_type
:canonical: algokit_subscriber.types.block.BlockValueDelta.action_type
:type: int
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.BlockValueDelta.action_type
```

````

````{py:attribute} bytes_value
:canonical: algokit_subscriber.types.block.BlockValueDelta.bytes_value
:type: typing_extensions.NotRequired[bytes]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.BlockValueDelta.bytes_value
```

````

````{py:attribute} uint_value
:canonical: algokit_subscriber.types.block.BlockValueDelta.uint_value
:type: typing_extensions.NotRequired[int]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.BlockValueDelta.uint_value
```

````

````{py:method} __contains__()
:canonical: algokit_subscriber.types.block.BlockValueDelta.__contains__

````

````{py:method} __delattr__()
:canonical: algokit_subscriber.types.block.BlockValueDelta.__delattr__

````

````{py:method} __delitem__()
:canonical: algokit_subscriber.types.block.BlockValueDelta.__delitem__

````

````{py:method} __dir__()
:canonical: algokit_subscriber.types.block.BlockValueDelta.__dir__

````

````{py:method} __eq__()
:canonical: algokit_subscriber.types.block.BlockValueDelta.__eq__

````

````{py:method} __format__()
:canonical: algokit_subscriber.types.block.BlockValueDelta.__format__

````

````{py:method} __ge__()
:canonical: algokit_subscriber.types.block.BlockValueDelta.__ge__

````

````{py:method} __getattribute__()
:canonical: algokit_subscriber.types.block.BlockValueDelta.__getattribute__

````

````{py:method} __getitem__()
:canonical: algokit_subscriber.types.block.BlockValueDelta.__getitem__

````

````{py:method} __getstate__()
:canonical: algokit_subscriber.types.block.BlockValueDelta.__getstate__

````

````{py:method} __gt__()
:canonical: algokit_subscriber.types.block.BlockValueDelta.__gt__

````

````{py:method} __ior__()
:canonical: algokit_subscriber.types.block.BlockValueDelta.__ior__

````

````{py:method} __iter__()
:canonical: algokit_subscriber.types.block.BlockValueDelta.__iter__

````

````{py:method} __le__()
:canonical: algokit_subscriber.types.block.BlockValueDelta.__le__

````

````{py:method} __len__()
:canonical: algokit_subscriber.types.block.BlockValueDelta.__len__

````

````{py:method} __lt__()
:canonical: algokit_subscriber.types.block.BlockValueDelta.__lt__

````

````{py:method} __ne__()
:canonical: algokit_subscriber.types.block.BlockValueDelta.__ne__

````

````{py:method} __new__()
:canonical: algokit_subscriber.types.block.BlockValueDelta.__new__

````

````{py:method} __or__()
:canonical: algokit_subscriber.types.block.BlockValueDelta.__or__

````

````{py:method} __reduce__()
:canonical: algokit_subscriber.types.block.BlockValueDelta.__reduce__

````

````{py:method} __reduce_ex__()
:canonical: algokit_subscriber.types.block.BlockValueDelta.__reduce_ex__

````

````{py:method} __repr__()
:canonical: algokit_subscriber.types.block.BlockValueDelta.__repr__

````

````{py:method} __reversed__()
:canonical: algokit_subscriber.types.block.BlockValueDelta.__reversed__

````

````{py:method} __ror__()
:canonical: algokit_subscriber.types.block.BlockValueDelta.__ror__

````

````{py:method} __setattr__()
:canonical: algokit_subscriber.types.block.BlockValueDelta.__setattr__

````

````{py:method} __setitem__()
:canonical: algokit_subscriber.types.block.BlockValueDelta.__setitem__

````

````{py:method} __sizeof__()
:canonical: algokit_subscriber.types.block.BlockValueDelta.__sizeof__

````

````{py:method} __str__()
:canonical: algokit_subscriber.types.block.BlockValueDelta.__str__

````

````{py:method} __subclasshook__()
:canonical: algokit_subscriber.types.block.BlockValueDelta.__subclasshook__

````

````{py:method} clear()
:canonical: algokit_subscriber.types.block.BlockValueDelta.clear

````

````{py:method} copy()
:canonical: algokit_subscriber.types.block.BlockValueDelta.copy

````

````{py:method} get()
:canonical: algokit_subscriber.types.block.BlockValueDelta.get

````

````{py:method} items()
:canonical: algokit_subscriber.types.block.BlockValueDelta.items

````

````{py:method} keys()
:canonical: algokit_subscriber.types.block.BlockValueDelta.keys

````

````{py:method} pop()
:canonical: algokit_subscriber.types.block.BlockValueDelta.pop

````

````{py:method} popitem()
:canonical: algokit_subscriber.types.block.BlockValueDelta.popitem

````

````{py:method} setdefault()
:canonical: algokit_subscriber.types.block.BlockValueDelta.setdefault

````

````{py:method} update()
:canonical: algokit_subscriber.types.block.BlockValueDelta.update

````

````{py:method} values()
:canonical: algokit_subscriber.types.block.BlockValueDelta.values

````

`````

`````{py:class} BlockTransactionEvalDelta()
:canonical: algokit_subscriber.types.block.BlockTransactionEvalDelta

Bases: {py:obj}`typing.TypedDict`

```{autodoc2-docstring} algokit_subscriber.types.block.BlockTransactionEvalDelta
```

```{rubric} Initialization
```

```{autodoc2-docstring} algokit_subscriber.types.block.BlockTransactionEvalDelta.__init__
```

````{py:attribute} gd
:canonical: algokit_subscriber.types.block.BlockTransactionEvalDelta.gd
:type: dict[str, algokit_subscriber.types.block.BlockValueDelta]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.BlockTransactionEvalDelta.gd
```

````

````{py:attribute} ld
:canonical: algokit_subscriber.types.block.BlockTransactionEvalDelta.ld
:type: dict[int, dict[str, algokit_subscriber.types.block.BlockValueDelta]]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.BlockTransactionEvalDelta.ld
```

````

````{py:attribute} lg
:canonical: algokit_subscriber.types.block.BlockTransactionEvalDelta.lg
:type: list[str]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.BlockTransactionEvalDelta.lg
```

````

````{py:attribute} itx
:canonical: algokit_subscriber.types.block.BlockTransactionEvalDelta.itx
:type: typing_extensions.NotRequired[list[BlockInnerTransaction]]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.BlockTransactionEvalDelta.itx
```

````

````{py:method} __contains__()
:canonical: algokit_subscriber.types.block.BlockTransactionEvalDelta.__contains__

````

````{py:method} __delattr__()
:canonical: algokit_subscriber.types.block.BlockTransactionEvalDelta.__delattr__

````

````{py:method} __delitem__()
:canonical: algokit_subscriber.types.block.BlockTransactionEvalDelta.__delitem__

````

````{py:method} __dir__()
:canonical: algokit_subscriber.types.block.BlockTransactionEvalDelta.__dir__

````

````{py:method} __eq__()
:canonical: algokit_subscriber.types.block.BlockTransactionEvalDelta.__eq__

````

````{py:method} __format__()
:canonical: algokit_subscriber.types.block.BlockTransactionEvalDelta.__format__

````

````{py:method} __ge__()
:canonical: algokit_subscriber.types.block.BlockTransactionEvalDelta.__ge__

````

````{py:method} __getattribute__()
:canonical: algokit_subscriber.types.block.BlockTransactionEvalDelta.__getattribute__

````

````{py:method} __getitem__()
:canonical: algokit_subscriber.types.block.BlockTransactionEvalDelta.__getitem__

````

````{py:method} __getstate__()
:canonical: algokit_subscriber.types.block.BlockTransactionEvalDelta.__getstate__

````

````{py:method} __gt__()
:canonical: algokit_subscriber.types.block.BlockTransactionEvalDelta.__gt__

````

````{py:method} __ior__()
:canonical: algokit_subscriber.types.block.BlockTransactionEvalDelta.__ior__

````

````{py:method} __iter__()
:canonical: algokit_subscriber.types.block.BlockTransactionEvalDelta.__iter__

````

````{py:method} __le__()
:canonical: algokit_subscriber.types.block.BlockTransactionEvalDelta.__le__

````

````{py:method} __len__()
:canonical: algokit_subscriber.types.block.BlockTransactionEvalDelta.__len__

````

````{py:method} __lt__()
:canonical: algokit_subscriber.types.block.BlockTransactionEvalDelta.__lt__

````

````{py:method} __ne__()
:canonical: algokit_subscriber.types.block.BlockTransactionEvalDelta.__ne__

````

````{py:method} __new__()
:canonical: algokit_subscriber.types.block.BlockTransactionEvalDelta.__new__

````

````{py:method} __or__()
:canonical: algokit_subscriber.types.block.BlockTransactionEvalDelta.__or__

````

````{py:method} __reduce__()
:canonical: algokit_subscriber.types.block.BlockTransactionEvalDelta.__reduce__

````

````{py:method} __reduce_ex__()
:canonical: algokit_subscriber.types.block.BlockTransactionEvalDelta.__reduce_ex__

````

````{py:method} __repr__()
:canonical: algokit_subscriber.types.block.BlockTransactionEvalDelta.__repr__

````

````{py:method} __reversed__()
:canonical: algokit_subscriber.types.block.BlockTransactionEvalDelta.__reversed__

````

````{py:method} __ror__()
:canonical: algokit_subscriber.types.block.BlockTransactionEvalDelta.__ror__

````

````{py:method} __setattr__()
:canonical: algokit_subscriber.types.block.BlockTransactionEvalDelta.__setattr__

````

````{py:method} __setitem__()
:canonical: algokit_subscriber.types.block.BlockTransactionEvalDelta.__setitem__

````

````{py:method} __sizeof__()
:canonical: algokit_subscriber.types.block.BlockTransactionEvalDelta.__sizeof__

````

````{py:method} __str__()
:canonical: algokit_subscriber.types.block.BlockTransactionEvalDelta.__str__

````

````{py:method} __subclasshook__()
:canonical: algokit_subscriber.types.block.BlockTransactionEvalDelta.__subclasshook__

````

````{py:method} clear()
:canonical: algokit_subscriber.types.block.BlockTransactionEvalDelta.clear

````

````{py:method} copy()
:canonical: algokit_subscriber.types.block.BlockTransactionEvalDelta.copy

````

````{py:method} get()
:canonical: algokit_subscriber.types.block.BlockTransactionEvalDelta.get

````

````{py:method} items()
:canonical: algokit_subscriber.types.block.BlockTransactionEvalDelta.items

````

````{py:method} keys()
:canonical: algokit_subscriber.types.block.BlockTransactionEvalDelta.keys

````

````{py:method} pop()
:canonical: algokit_subscriber.types.block.BlockTransactionEvalDelta.pop

````

````{py:method} popitem()
:canonical: algokit_subscriber.types.block.BlockTransactionEvalDelta.popitem

````

````{py:method} setdefault()
:canonical: algokit_subscriber.types.block.BlockTransactionEvalDelta.setdefault

````

````{py:method} update()
:canonical: algokit_subscriber.types.block.BlockTransactionEvalDelta.update

````

````{py:method} values()
:canonical: algokit_subscriber.types.block.BlockTransactionEvalDelta.values

````

`````

````{py:data} LogicSig
:canonical: algokit_subscriber.types.block.LogicSig
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.LogicSig
```

````

````{py:data} MultisigSig
:canonical: algokit_subscriber.types.block.MultisigSig
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.MultisigSig
```

````

`````{py:class} TransactionInBlock()
:canonical: algokit_subscriber.types.block.TransactionInBlock

Bases: {py:obj}`typing.TypedDict`

```{autodoc2-docstring} algokit_subscriber.types.block.TransactionInBlock
```

```{rubric} Initialization
```

```{autodoc2-docstring} algokit_subscriber.types.block.TransactionInBlock.__init__
```

````{py:attribute} block_transaction
:canonical: algokit_subscriber.types.block.TransactionInBlock.block_transaction
:type: BlockTransaction | BlockInnerTransaction
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.TransactionInBlock.block_transaction
```

````

````{py:attribute} round_offset
:canonical: algokit_subscriber.types.block.TransactionInBlock.round_offset
:type: int
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.TransactionInBlock.round_offset
```

````

````{py:attribute} round_index
:canonical: algokit_subscriber.types.block.TransactionInBlock.round_index
:type: int
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.TransactionInBlock.round_index
```

````

````{py:attribute} parent_transaction_id
:canonical: algokit_subscriber.types.block.TransactionInBlock.parent_transaction_id
:type: typing_extensions.NotRequired[None | str]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.TransactionInBlock.parent_transaction_id
```

````

````{py:attribute} parent_offset
:canonical: algokit_subscriber.types.block.TransactionInBlock.parent_offset
:type: typing_extensions.NotRequired[None | int]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.TransactionInBlock.parent_offset
```

````

````{py:attribute} genesis_hash
:canonical: algokit_subscriber.types.block.TransactionInBlock.genesis_hash
:type: bytes
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.TransactionInBlock.genesis_hash
```

````

````{py:attribute} genesis_id
:canonical: algokit_subscriber.types.block.TransactionInBlock.genesis_id
:type: str
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.TransactionInBlock.genesis_id
```

````

````{py:attribute} round_number
:canonical: algokit_subscriber.types.block.TransactionInBlock.round_number
:type: int
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.TransactionInBlock.round_number
```

````

````{py:attribute} round_timestamp
:canonical: algokit_subscriber.types.block.TransactionInBlock.round_timestamp
:type: int
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.TransactionInBlock.round_timestamp
```

````

````{py:attribute} transaction
:canonical: algokit_subscriber.types.block.TransactionInBlock.transaction
:type: algosdk.transaction.Transaction
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.TransactionInBlock.transaction
```

````

````{py:attribute} created_asset_id
:canonical: algokit_subscriber.types.block.TransactionInBlock.created_asset_id
:type: typing_extensions.NotRequired[None | int]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.TransactionInBlock.created_asset_id
```

````

````{py:attribute} created_app_id
:canonical: algokit_subscriber.types.block.TransactionInBlock.created_app_id
:type: typing_extensions.NotRequired[None | int]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.TransactionInBlock.created_app_id
```

````

````{py:attribute} asset_close_amount
:canonical: algokit_subscriber.types.block.TransactionInBlock.asset_close_amount
:type: typing_extensions.NotRequired[None | int]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.TransactionInBlock.asset_close_amount
```

````

````{py:attribute} close_amount
:canonical: algokit_subscriber.types.block.TransactionInBlock.close_amount
:type: typing_extensions.NotRequired[None | int]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.TransactionInBlock.close_amount
```

````

````{py:attribute} logs
:canonical: algokit_subscriber.types.block.TransactionInBlock.logs
:type: typing_extensions.NotRequired[None | list[str]]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.TransactionInBlock.logs
```

````

````{py:method} __contains__()
:canonical: algokit_subscriber.types.block.TransactionInBlock.__contains__

````

````{py:method} __delattr__()
:canonical: algokit_subscriber.types.block.TransactionInBlock.__delattr__

````

````{py:method} __delitem__()
:canonical: algokit_subscriber.types.block.TransactionInBlock.__delitem__

````

````{py:method} __dir__()
:canonical: algokit_subscriber.types.block.TransactionInBlock.__dir__

````

````{py:method} __eq__()
:canonical: algokit_subscriber.types.block.TransactionInBlock.__eq__

````

````{py:method} __format__()
:canonical: algokit_subscriber.types.block.TransactionInBlock.__format__

````

````{py:method} __ge__()
:canonical: algokit_subscriber.types.block.TransactionInBlock.__ge__

````

````{py:method} __getattribute__()
:canonical: algokit_subscriber.types.block.TransactionInBlock.__getattribute__

````

````{py:method} __getitem__()
:canonical: algokit_subscriber.types.block.TransactionInBlock.__getitem__

````

````{py:method} __getstate__()
:canonical: algokit_subscriber.types.block.TransactionInBlock.__getstate__

````

````{py:method} __gt__()
:canonical: algokit_subscriber.types.block.TransactionInBlock.__gt__

````

````{py:method} __ior__()
:canonical: algokit_subscriber.types.block.TransactionInBlock.__ior__

````

````{py:method} __iter__()
:canonical: algokit_subscriber.types.block.TransactionInBlock.__iter__

````

````{py:method} __le__()
:canonical: algokit_subscriber.types.block.TransactionInBlock.__le__

````

````{py:method} __len__()
:canonical: algokit_subscriber.types.block.TransactionInBlock.__len__

````

````{py:method} __lt__()
:canonical: algokit_subscriber.types.block.TransactionInBlock.__lt__

````

````{py:method} __ne__()
:canonical: algokit_subscriber.types.block.TransactionInBlock.__ne__

````

````{py:method} __new__()
:canonical: algokit_subscriber.types.block.TransactionInBlock.__new__

````

````{py:method} __or__()
:canonical: algokit_subscriber.types.block.TransactionInBlock.__or__

````

````{py:method} __reduce__()
:canonical: algokit_subscriber.types.block.TransactionInBlock.__reduce__

````

````{py:method} __reduce_ex__()
:canonical: algokit_subscriber.types.block.TransactionInBlock.__reduce_ex__

````

````{py:method} __repr__()
:canonical: algokit_subscriber.types.block.TransactionInBlock.__repr__

````

````{py:method} __reversed__()
:canonical: algokit_subscriber.types.block.TransactionInBlock.__reversed__

````

````{py:method} __ror__()
:canonical: algokit_subscriber.types.block.TransactionInBlock.__ror__

````

````{py:method} __setattr__()
:canonical: algokit_subscriber.types.block.TransactionInBlock.__setattr__

````

````{py:method} __setitem__()
:canonical: algokit_subscriber.types.block.TransactionInBlock.__setitem__

````

````{py:method} __sizeof__()
:canonical: algokit_subscriber.types.block.TransactionInBlock.__sizeof__

````

````{py:method} __str__()
:canonical: algokit_subscriber.types.block.TransactionInBlock.__str__

````

````{py:method} __subclasshook__()
:canonical: algokit_subscriber.types.block.TransactionInBlock.__subclasshook__

````

````{py:method} clear()
:canonical: algokit_subscriber.types.block.TransactionInBlock.clear

````

````{py:method} copy()
:canonical: algokit_subscriber.types.block.TransactionInBlock.copy

````

````{py:method} get()
:canonical: algokit_subscriber.types.block.TransactionInBlock.get

````

````{py:method} items()
:canonical: algokit_subscriber.types.block.TransactionInBlock.items

````

````{py:method} keys()
:canonical: algokit_subscriber.types.block.TransactionInBlock.keys

````

````{py:method} pop()
:canonical: algokit_subscriber.types.block.TransactionInBlock.pop

````

````{py:method} popitem()
:canonical: algokit_subscriber.types.block.TransactionInBlock.popitem

````

````{py:method} setdefault()
:canonical: algokit_subscriber.types.block.TransactionInBlock.setdefault

````

````{py:method} update()
:canonical: algokit_subscriber.types.block.TransactionInBlock.update

````

````{py:method} values()
:canonical: algokit_subscriber.types.block.TransactionInBlock.values

````

`````

`````{py:class} BlockInnerTransaction()
:canonical: algokit_subscriber.types.block.BlockInnerTransaction

Bases: {py:obj}`typing.TypedDict`

````{py:attribute} txn
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.txn
:type: dict[str, typing.Any]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.BlockInnerTransaction.txn
```

````

````{py:attribute} dt
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.dt
:type: typing_extensions.NotRequired[None | algokit_subscriber.types.block.BlockTransactionEvalDelta]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.BlockInnerTransaction.dt
```

````

````{py:attribute} caid
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.caid
:type: typing_extensions.NotRequired[None | int]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.BlockInnerTransaction.caid
```

````

````{py:attribute} apid
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.apid
:type: typing_extensions.NotRequired[None | int]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.BlockInnerTransaction.apid
```

````

````{py:attribute} aca
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.aca
:type: typing_extensions.NotRequired[None | int]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.BlockInnerTransaction.aca
```

````

````{py:attribute} ca
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.ca
:type: typing_extensions.NotRequired[None | int]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.BlockInnerTransaction.ca
```

````

````{py:attribute} sig
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.sig
:type: typing_extensions.NotRequired[None | bytes]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.BlockInnerTransaction.sig
```

````

````{py:attribute} lsig
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.lsig
:type: typing_extensions.NotRequired[None | algokit_subscriber.types.block.LogicSig]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.BlockInnerTransaction.lsig
```

````

````{py:attribute} msig
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.msig
:type: typing_extensions.NotRequired[None | algokit_subscriber.types.block.MultisigSig]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.BlockInnerTransaction.msig
```

````

````{py:attribute} sgnr
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.sgnr
:type: typing_extensions.NotRequired[None | bytes]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.BlockInnerTransaction.sgnr
```

````

````{py:method} __contains__()
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.__contains__

````

````{py:method} __delattr__()
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.__delattr__

````

````{py:method} __delitem__()
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.__delitem__

````

````{py:method} __dir__()
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.__dir__

````

````{py:method} __eq__()
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.__eq__

````

````{py:method} __format__()
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.__format__

````

````{py:method} __ge__()
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.__ge__

````

````{py:method} __getattribute__()
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.__getattribute__

````

````{py:method} __getitem__()
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.__getitem__

````

````{py:method} __getstate__()
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.__getstate__

````

````{py:method} __gt__()
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.__gt__

````

````{py:method} __ior__()
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.__ior__

````

````{py:method} __iter__()
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.__iter__

````

````{py:method} __le__()
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.__le__

````

````{py:method} __len__()
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.__len__

````

````{py:method} __lt__()
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.__lt__

````

````{py:method} __ne__()
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.__ne__

````

````{py:method} __new__()
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.__new__

````

````{py:method} __or__()
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.__or__

````

````{py:method} __reduce__()
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.__reduce__

````

````{py:method} __reduce_ex__()
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.__reduce_ex__

````

````{py:method} __repr__()
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.__repr__

````

````{py:method} __reversed__()
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.__reversed__

````

````{py:method} __ror__()
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.__ror__

````

````{py:method} __setattr__()
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.__setattr__

````

````{py:method} __setitem__()
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.__setitem__

````

````{py:method} __sizeof__()
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.__sizeof__

````

````{py:method} __str__()
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.__str__

````

````{py:method} __subclasshook__()
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.__subclasshook__

````

````{py:method} clear()
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.clear

````

````{py:method} copy()
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.copy

````

````{py:method} get()
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.get

````

````{py:method} items()
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.items

````

````{py:method} keys()
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.keys

````

````{py:method} pop()
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.pop

````

````{py:method} popitem()
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.popitem

````

````{py:method} setdefault()
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.setdefault

````

````{py:method} update()
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.update

````

````{py:method} values()
:canonical: algokit_subscriber.types.block.BlockInnerTransaction.values

````

`````

`````{py:class} BlockTransaction()
:canonical: algokit_subscriber.types.block.BlockTransaction

Bases: {py:obj}`algokit_subscriber.types.block.BlockInnerTransaction`

```{autodoc2-docstring} algokit_subscriber.types.block.BlockTransaction
```

```{rubric} Initialization
```

```{autodoc2-docstring} algokit_subscriber.types.block.BlockTransaction.__init__
```

````{py:attribute} hgi
:canonical: algokit_subscriber.types.block.BlockTransaction.hgi
:type: typing_extensions.NotRequired[None | bool]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.BlockTransaction.hgi
```

````

````{py:attribute} hgh
:canonical: algokit_subscriber.types.block.BlockTransaction.hgh
:type: typing_extensions.NotRequired[None | bool]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.BlockTransaction.hgh
```

````

````{py:attribute} txn
:canonical: algokit_subscriber.types.block.BlockTransaction.txn
:type: dict[str, typing.Any]
:value: >
   None

````

````{py:attribute} dt
:canonical: algokit_subscriber.types.block.BlockTransaction.dt
:type: typing_extensions.NotRequired[None | algokit_subscriber.types.block.BlockTransactionEvalDelta]
:value: >
   None

````

````{py:attribute} caid
:canonical: algokit_subscriber.types.block.BlockTransaction.caid
:type: typing_extensions.NotRequired[None | int]
:value: >
   None

````

````{py:attribute} apid
:canonical: algokit_subscriber.types.block.BlockTransaction.apid
:type: typing_extensions.NotRequired[None | int]
:value: >
   None

````

````{py:attribute} aca
:canonical: algokit_subscriber.types.block.BlockTransaction.aca
:type: typing_extensions.NotRequired[None | int]
:value: >
   None

````

````{py:attribute} ca
:canonical: algokit_subscriber.types.block.BlockTransaction.ca
:type: typing_extensions.NotRequired[None | int]
:value: >
   None

````

````{py:attribute} sig
:canonical: algokit_subscriber.types.block.BlockTransaction.sig
:type: typing_extensions.NotRequired[None | bytes]
:value: >
   None

````

````{py:attribute} lsig
:canonical: algokit_subscriber.types.block.BlockTransaction.lsig
:type: typing_extensions.NotRequired[None | algokit_subscriber.types.block.LogicSig]
:value: >
   None

````

````{py:attribute} msig
:canonical: algokit_subscriber.types.block.BlockTransaction.msig
:type: typing_extensions.NotRequired[None | algokit_subscriber.types.block.MultisigSig]
:value: >
   None

````

````{py:attribute} sgnr
:canonical: algokit_subscriber.types.block.BlockTransaction.sgnr
:type: typing_extensions.NotRequired[None | bytes]
:value: >
   None

````

````{py:method} __contains__()
:canonical: algokit_subscriber.types.block.BlockTransaction.__contains__

````

````{py:method} __delattr__()
:canonical: algokit_subscriber.types.block.BlockTransaction.__delattr__

````

````{py:method} __delitem__()
:canonical: algokit_subscriber.types.block.BlockTransaction.__delitem__

````

````{py:method} __dir__()
:canonical: algokit_subscriber.types.block.BlockTransaction.__dir__

````

````{py:method} __eq__()
:canonical: algokit_subscriber.types.block.BlockTransaction.__eq__

````

````{py:method} __format__()
:canonical: algokit_subscriber.types.block.BlockTransaction.__format__

````

````{py:method} __ge__()
:canonical: algokit_subscriber.types.block.BlockTransaction.__ge__

````

````{py:method} __getattribute__()
:canonical: algokit_subscriber.types.block.BlockTransaction.__getattribute__

````

````{py:method} __getitem__()
:canonical: algokit_subscriber.types.block.BlockTransaction.__getitem__

````

````{py:method} __getstate__()
:canonical: algokit_subscriber.types.block.BlockTransaction.__getstate__

````

````{py:method} __gt__()
:canonical: algokit_subscriber.types.block.BlockTransaction.__gt__

````

````{py:method} __ior__()
:canonical: algokit_subscriber.types.block.BlockTransaction.__ior__

````

````{py:method} __iter__()
:canonical: algokit_subscriber.types.block.BlockTransaction.__iter__

````

````{py:method} __le__()
:canonical: algokit_subscriber.types.block.BlockTransaction.__le__

````

````{py:method} __len__()
:canonical: algokit_subscriber.types.block.BlockTransaction.__len__

````

````{py:method} __lt__()
:canonical: algokit_subscriber.types.block.BlockTransaction.__lt__

````

````{py:method} __ne__()
:canonical: algokit_subscriber.types.block.BlockTransaction.__ne__

````

````{py:method} __new__()
:canonical: algokit_subscriber.types.block.BlockTransaction.__new__

````

````{py:method} __or__()
:canonical: algokit_subscriber.types.block.BlockTransaction.__or__

````

````{py:method} __reduce__()
:canonical: algokit_subscriber.types.block.BlockTransaction.__reduce__

````

````{py:method} __reduce_ex__()
:canonical: algokit_subscriber.types.block.BlockTransaction.__reduce_ex__

````

````{py:method} __repr__()
:canonical: algokit_subscriber.types.block.BlockTransaction.__repr__

````

````{py:method} __reversed__()
:canonical: algokit_subscriber.types.block.BlockTransaction.__reversed__

````

````{py:method} __ror__()
:canonical: algokit_subscriber.types.block.BlockTransaction.__ror__

````

````{py:method} __setattr__()
:canonical: algokit_subscriber.types.block.BlockTransaction.__setattr__

````

````{py:method} __setitem__()
:canonical: algokit_subscriber.types.block.BlockTransaction.__setitem__

````

````{py:method} __sizeof__()
:canonical: algokit_subscriber.types.block.BlockTransaction.__sizeof__

````

````{py:method} __str__()
:canonical: algokit_subscriber.types.block.BlockTransaction.__str__

````

````{py:method} __subclasshook__()
:canonical: algokit_subscriber.types.block.BlockTransaction.__subclasshook__

````

````{py:method} clear()
:canonical: algokit_subscriber.types.block.BlockTransaction.clear

````

````{py:method} copy()
:canonical: algokit_subscriber.types.block.BlockTransaction.copy

````

````{py:method} get()
:canonical: algokit_subscriber.types.block.BlockTransaction.get

````

````{py:method} items()
:canonical: algokit_subscriber.types.block.BlockTransaction.items

````

````{py:method} keys()
:canonical: algokit_subscriber.types.block.BlockTransaction.keys

````

````{py:method} pop()
:canonical: algokit_subscriber.types.block.BlockTransaction.pop

````

````{py:method} popitem()
:canonical: algokit_subscriber.types.block.BlockTransaction.popitem

````

````{py:method} setdefault()
:canonical: algokit_subscriber.types.block.BlockTransaction.setdefault

````

````{py:method} update()
:canonical: algokit_subscriber.types.block.BlockTransaction.update

````

````{py:method} values()
:canonical: algokit_subscriber.types.block.BlockTransaction.values

````

`````

````{py:data} BlockAgreementCertificate
:canonical: algokit_subscriber.types.block.BlockAgreementCertificate
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.BlockAgreementCertificate
```

````

`````{py:class} Block()
:canonical: algokit_subscriber.types.block.Block

Bases: {py:obj}`typing.TypedDict`

```{autodoc2-docstring} algokit_subscriber.types.block.Block
```

```{rubric} Initialization
```

```{autodoc2-docstring} algokit_subscriber.types.block.Block.__init__
```

````{py:attribute} earn
:canonical: algokit_subscriber.types.block.Block.earn
:type: int
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.Block.earn
```

````

````{py:attribute} fees
:canonical: algokit_subscriber.types.block.Block.fees
:type: bytes
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.Block.fees
```

````

````{py:attribute} frac
:canonical: algokit_subscriber.types.block.Block.frac
:type: int
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.Block.frac
```

````

````{py:attribute} gen
:canonical: algokit_subscriber.types.block.Block.gen
:type: str
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.Block.gen
```

````

````{py:attribute} gh
:canonical: algokit_subscriber.types.block.Block.gh
:type: bytes
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.Block.gh
```

````

````{py:attribute} prev
:canonical: algokit_subscriber.types.block.Block.prev
:type: typing_extensions.NotRequired[None | bytes]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.Block.prev
```

````

````{py:attribute} proto
:canonical: algokit_subscriber.types.block.Block.proto
:type: str
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.Block.proto
```

````

````{py:attribute} rate
:canonical: algokit_subscriber.types.block.Block.rate
:type: typing_extensions.NotRequired[None | int]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.Block.rate
```

````

````{py:attribute} rnd
:canonical: algokit_subscriber.types.block.Block.rnd
:type: int
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.Block.rnd
```

````

````{py:attribute} rwcalr
:canonical: algokit_subscriber.types.block.Block.rwcalr
:type: int
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.Block.rwcalr
```

````

````{py:attribute} rwd
:canonical: algokit_subscriber.types.block.Block.rwd
:type: bytes
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.Block.rwd
```

````

````{py:attribute} seed
:canonical: algokit_subscriber.types.block.Block.seed
:type: bytes
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.Block.seed
```

````

````{py:attribute} tc
:canonical: algokit_subscriber.types.block.Block.tc
:type: int
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.Block.tc
```

````

````{py:attribute} ts
:canonical: algokit_subscriber.types.block.Block.ts
:type: int
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.Block.ts
```

````

````{py:attribute} txn
:canonical: algokit_subscriber.types.block.Block.txn
:type: bytes
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.Block.txn
```

````

````{py:attribute} txn256
:canonical: algokit_subscriber.types.block.Block.txn256
:type: str
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.Block.txn256
```

````

````{py:attribute} nextproto
:canonical: algokit_subscriber.types.block.Block.nextproto
:type: typing_extensions.NotRequired[None | str]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.Block.nextproto
```

````

````{py:attribute} nextyes
:canonical: algokit_subscriber.types.block.Block.nextyes
:type: typing_extensions.NotRequired[None | int]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.Block.nextyes
```

````

````{py:attribute} nextbefore
:canonical: algokit_subscriber.types.block.Block.nextbefore
:type: typing_extensions.NotRequired[None | int]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.Block.nextbefore
```

````

````{py:attribute} nextswitch
:canonical: algokit_subscriber.types.block.Block.nextswitch
:type: typing_extensions.NotRequired[None | int]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.Block.nextswitch
```

````

````{py:attribute} txns
:canonical: algokit_subscriber.types.block.Block.txns
:type: typing_extensions.NotRequired[None | list[algokit_subscriber.types.block.BlockTransaction]]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.Block.txns
```

````

````{py:attribute} prp
:canonical: algokit_subscriber.types.block.Block.prp
:type: typing_extensions.NotRequired[None | bytes]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.Block.prp
```

````

````{py:attribute} fc
:canonical: algokit_subscriber.types.block.Block.fc
:type: typing_extensions.NotRequired[None | int]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.Block.fc
```

````

````{py:attribute} bi
:canonical: algokit_subscriber.types.block.Block.bi
:type: typing_extensions.NotRequired[None | int]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.Block.bi
```

````

````{py:attribute} pp
:canonical: algokit_subscriber.types.block.Block.pp
:type: typing_extensions.NotRequired[None | int]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.Block.pp
```

````

````{py:method} __contains__()
:canonical: algokit_subscriber.types.block.Block.__contains__

````

````{py:method} __delattr__()
:canonical: algokit_subscriber.types.block.Block.__delattr__

````

````{py:method} __delitem__()
:canonical: algokit_subscriber.types.block.Block.__delitem__

````

````{py:method} __dir__()
:canonical: algokit_subscriber.types.block.Block.__dir__

````

````{py:method} __eq__()
:canonical: algokit_subscriber.types.block.Block.__eq__

````

````{py:method} __format__()
:canonical: algokit_subscriber.types.block.Block.__format__

````

````{py:method} __ge__()
:canonical: algokit_subscriber.types.block.Block.__ge__

````

````{py:method} __getattribute__()
:canonical: algokit_subscriber.types.block.Block.__getattribute__

````

````{py:method} __getitem__()
:canonical: algokit_subscriber.types.block.Block.__getitem__

````

````{py:method} __getstate__()
:canonical: algokit_subscriber.types.block.Block.__getstate__

````

````{py:method} __gt__()
:canonical: algokit_subscriber.types.block.Block.__gt__

````

````{py:method} __ior__()
:canonical: algokit_subscriber.types.block.Block.__ior__

````

````{py:method} __iter__()
:canonical: algokit_subscriber.types.block.Block.__iter__

````

````{py:method} __le__()
:canonical: algokit_subscriber.types.block.Block.__le__

````

````{py:method} __len__()
:canonical: algokit_subscriber.types.block.Block.__len__

````

````{py:method} __lt__()
:canonical: algokit_subscriber.types.block.Block.__lt__

````

````{py:method} __ne__()
:canonical: algokit_subscriber.types.block.Block.__ne__

````

````{py:method} __new__()
:canonical: algokit_subscriber.types.block.Block.__new__

````

````{py:method} __or__()
:canonical: algokit_subscriber.types.block.Block.__or__

````

````{py:method} __reduce__()
:canonical: algokit_subscriber.types.block.Block.__reduce__

````

````{py:method} __reduce_ex__()
:canonical: algokit_subscriber.types.block.Block.__reduce_ex__

````

````{py:method} __repr__()
:canonical: algokit_subscriber.types.block.Block.__repr__

````

````{py:method} __reversed__()
:canonical: algokit_subscriber.types.block.Block.__reversed__

````

````{py:method} __ror__()
:canonical: algokit_subscriber.types.block.Block.__ror__

````

````{py:method} __setattr__()
:canonical: algokit_subscriber.types.block.Block.__setattr__

````

````{py:method} __setitem__()
:canonical: algokit_subscriber.types.block.Block.__setitem__

````

````{py:method} __sizeof__()
:canonical: algokit_subscriber.types.block.Block.__sizeof__

````

````{py:method} __str__()
:canonical: algokit_subscriber.types.block.Block.__str__

````

````{py:method} __subclasshook__()
:canonical: algokit_subscriber.types.block.Block.__subclasshook__

````

````{py:method} clear()
:canonical: algokit_subscriber.types.block.Block.clear

````

````{py:method} copy()
:canonical: algokit_subscriber.types.block.Block.copy

````

````{py:method} get()
:canonical: algokit_subscriber.types.block.Block.get

````

````{py:method} items()
:canonical: algokit_subscriber.types.block.Block.items

````

````{py:method} keys()
:canonical: algokit_subscriber.types.block.Block.keys

````

````{py:method} pop()
:canonical: algokit_subscriber.types.block.Block.pop

````

````{py:method} popitem()
:canonical: algokit_subscriber.types.block.Block.popitem

````

````{py:method} setdefault()
:canonical: algokit_subscriber.types.block.Block.setdefault

````

````{py:method} update()
:canonical: algokit_subscriber.types.block.Block.update

````

````{py:method} values()
:canonical: algokit_subscriber.types.block.Block.values

````

`````

`````{py:class} BlockData()
:canonical: algokit_subscriber.types.block.BlockData

Bases: {py:obj}`typing.TypedDict`

```{autodoc2-docstring} algokit_subscriber.types.block.BlockData
```

```{rubric} Initialization
```

```{autodoc2-docstring} algokit_subscriber.types.block.BlockData.__init__
```

````{py:attribute} block
:canonical: algokit_subscriber.types.block.BlockData.block
:type: algokit_subscriber.types.block.Block
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.BlockData.block
```

````

````{py:attribute} cert
:canonical: algokit_subscriber.types.block.BlockData.cert
:type: algokit_subscriber.types.block.BlockAgreementCertificate
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.block.BlockData.cert
```

````

````{py:method} __contains__()
:canonical: algokit_subscriber.types.block.BlockData.__contains__

````

````{py:method} __delattr__()
:canonical: algokit_subscriber.types.block.BlockData.__delattr__

````

````{py:method} __delitem__()
:canonical: algokit_subscriber.types.block.BlockData.__delitem__

````

````{py:method} __dir__()
:canonical: algokit_subscriber.types.block.BlockData.__dir__

````

````{py:method} __eq__()
:canonical: algokit_subscriber.types.block.BlockData.__eq__

````

````{py:method} __format__()
:canonical: algokit_subscriber.types.block.BlockData.__format__

````

````{py:method} __ge__()
:canonical: algokit_subscriber.types.block.BlockData.__ge__

````

````{py:method} __getattribute__()
:canonical: algokit_subscriber.types.block.BlockData.__getattribute__

````

````{py:method} __getitem__()
:canonical: algokit_subscriber.types.block.BlockData.__getitem__

````

````{py:method} __getstate__()
:canonical: algokit_subscriber.types.block.BlockData.__getstate__

````

````{py:method} __gt__()
:canonical: algokit_subscriber.types.block.BlockData.__gt__

````

````{py:method} __ior__()
:canonical: algokit_subscriber.types.block.BlockData.__ior__

````

````{py:method} __iter__()
:canonical: algokit_subscriber.types.block.BlockData.__iter__

````

````{py:method} __le__()
:canonical: algokit_subscriber.types.block.BlockData.__le__

````

````{py:method} __len__()
:canonical: algokit_subscriber.types.block.BlockData.__len__

````

````{py:method} __lt__()
:canonical: algokit_subscriber.types.block.BlockData.__lt__

````

````{py:method} __ne__()
:canonical: algokit_subscriber.types.block.BlockData.__ne__

````

````{py:method} __new__()
:canonical: algokit_subscriber.types.block.BlockData.__new__

````

````{py:method} __or__()
:canonical: algokit_subscriber.types.block.BlockData.__or__

````

````{py:method} __reduce__()
:canonical: algokit_subscriber.types.block.BlockData.__reduce__

````

````{py:method} __reduce_ex__()
:canonical: algokit_subscriber.types.block.BlockData.__reduce_ex__

````

````{py:method} __repr__()
:canonical: algokit_subscriber.types.block.BlockData.__repr__

````

````{py:method} __reversed__()
:canonical: algokit_subscriber.types.block.BlockData.__reversed__

````

````{py:method} __ror__()
:canonical: algokit_subscriber.types.block.BlockData.__ror__

````

````{py:method} __setattr__()
:canonical: algokit_subscriber.types.block.BlockData.__setattr__

````

````{py:method} __setitem__()
:canonical: algokit_subscriber.types.block.BlockData.__setitem__

````

````{py:method} __sizeof__()
:canonical: algokit_subscriber.types.block.BlockData.__sizeof__

````

````{py:method} __str__()
:canonical: algokit_subscriber.types.block.BlockData.__str__

````

````{py:method} __subclasshook__()
:canonical: algokit_subscriber.types.block.BlockData.__subclasshook__

````

````{py:method} clear()
:canonical: algokit_subscriber.types.block.BlockData.clear

````

````{py:method} copy()
:canonical: algokit_subscriber.types.block.BlockData.copy

````

````{py:method} get()
:canonical: algokit_subscriber.types.block.BlockData.get

````

````{py:method} items()
:canonical: algokit_subscriber.types.block.BlockData.items

````

````{py:method} keys()
:canonical: algokit_subscriber.types.block.BlockData.keys

````

````{py:method} pop()
:canonical: algokit_subscriber.types.block.BlockData.pop

````

````{py:method} popitem()
:canonical: algokit_subscriber.types.block.BlockData.popitem

````

````{py:method} setdefault()
:canonical: algokit_subscriber.types.block.BlockData.setdefault

````

````{py:method} update()
:canonical: algokit_subscriber.types.block.BlockData.update

````

````{py:method} values()
:canonical: algokit_subscriber.types.block.BlockData.values

````

`````
