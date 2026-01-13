# {py:mod}`algokit_subscriber.types.transaction`

```{py:module} algokit_subscriber.types.transaction
```

```{autodoc2-docstring} algokit_subscriber.types.transaction
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TransactionType <algokit_subscriber.types.transaction.TransactionType>`
  - ```{autodoc2-docstring} algokit_subscriber.types.transaction.TransactionType
    :summary:
    ```
* - {py:obj}`AlgodOnComplete <algokit_subscriber.types.transaction.AlgodOnComplete>`
  - ```{autodoc2-docstring} algokit_subscriber.types.transaction.AlgodOnComplete
    :summary:
    ```
* - {py:obj}`IndexerOnComplete <algokit_subscriber.types.transaction.IndexerOnComplete>`
  - ```{autodoc2-docstring} algokit_subscriber.types.transaction.IndexerOnComplete
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`AnyTransaction <algokit_subscriber.types.transaction.AnyTransaction>`
  - ```{autodoc2-docstring} algokit_subscriber.types.transaction.AnyTransaction
    :summary:
    ```
````

### API

````{py:data} AnyTransaction
:canonical: algokit_subscriber.types.transaction.AnyTransaction
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.transaction.AnyTransaction
```

````

`````{py:class} TransactionType(*args, **kwds)
:canonical: algokit_subscriber.types.transaction.TransactionType

Bases: {py:obj}`enum.Enum`

```{autodoc2-docstring} algokit_subscriber.types.transaction.TransactionType
```

```{rubric} Initialization
```

```{autodoc2-docstring} algokit_subscriber.types.transaction.TransactionType.__init__
```

````{py:attribute} pay
:canonical: algokit_subscriber.types.transaction.TransactionType.pay
:value: >
   'pay'

```{autodoc2-docstring} algokit_subscriber.types.transaction.TransactionType.pay
```

````

````{py:attribute} keyreg
:canonical: algokit_subscriber.types.transaction.TransactionType.keyreg
:value: >
   'keyreg'

```{autodoc2-docstring} algokit_subscriber.types.transaction.TransactionType.keyreg
```

````

````{py:attribute} acfg
:canonical: algokit_subscriber.types.transaction.TransactionType.acfg
:value: >
   'acfg'

```{autodoc2-docstring} algokit_subscriber.types.transaction.TransactionType.acfg
```

````

````{py:attribute} axfer
:canonical: algokit_subscriber.types.transaction.TransactionType.axfer
:value: >
   'axfer'

```{autodoc2-docstring} algokit_subscriber.types.transaction.TransactionType.axfer
```

````

````{py:attribute} afrz
:canonical: algokit_subscriber.types.transaction.TransactionType.afrz
:value: >
   'afrz'

```{autodoc2-docstring} algokit_subscriber.types.transaction.TransactionType.afrz
```

````

````{py:attribute} appl
:canonical: algokit_subscriber.types.transaction.TransactionType.appl
:value: >
   'appl'

```{autodoc2-docstring} algokit_subscriber.types.transaction.TransactionType.appl
```

````

````{py:attribute} stpf
:canonical: algokit_subscriber.types.transaction.TransactionType.stpf
:value: >
   'stpf'

```{autodoc2-docstring} algokit_subscriber.types.transaction.TransactionType.stpf
```

````

````{py:attribute} hb
:canonical: algokit_subscriber.types.transaction.TransactionType.hb
:value: >
   'hb'

```{autodoc2-docstring} algokit_subscriber.types.transaction.TransactionType.hb
```

````

````{py:method} __signature__()
:canonical: algokit_subscriber.types.transaction.TransactionType.__signature__
:classmethod:

````

````{py:method} __new__(value)
:canonical: algokit_subscriber.types.transaction.TransactionType.__new__

````

````{py:method} __repr__()
:canonical: algokit_subscriber.types.transaction.TransactionType.__repr__

````

````{py:method} __str__()
:canonical: algokit_subscriber.types.transaction.TransactionType.__str__

````

````{py:method} __dir__()
:canonical: algokit_subscriber.types.transaction.TransactionType.__dir__

````

````{py:method} __format__(format_spec)
:canonical: algokit_subscriber.types.transaction.TransactionType.__format__

````

````{py:method} __hash__()
:canonical: algokit_subscriber.types.transaction.TransactionType.__hash__

````

````{py:method} __reduce_ex__(proto)
:canonical: algokit_subscriber.types.transaction.TransactionType.__reduce_ex__

````

````{py:method} __deepcopy__(memo)
:canonical: algokit_subscriber.types.transaction.TransactionType.__deepcopy__

````

````{py:method} __copy__()
:canonical: algokit_subscriber.types.transaction.TransactionType.__copy__

````

````{py:method} name()
:canonical: algokit_subscriber.types.transaction.TransactionType.name

````

````{py:method} value()
:canonical: algokit_subscriber.types.transaction.TransactionType.value

````

`````

`````{py:class} AlgodOnComplete()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete

Bases: {py:obj}`enum.IntEnum`

```{autodoc2-docstring} algokit_subscriber.types.transaction.AlgodOnComplete
```

```{rubric} Initialization
```

```{autodoc2-docstring} algokit_subscriber.types.transaction.AlgodOnComplete.__init__
```

````{py:attribute} NoOpOC
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.NoOpOC
:value: >
   0

```{autodoc2-docstring} algokit_subscriber.types.transaction.AlgodOnComplete.NoOpOC
```

````

````{py:attribute} OptInOC
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.OptInOC
:value: >
   1

```{autodoc2-docstring} algokit_subscriber.types.transaction.AlgodOnComplete.OptInOC
```

````

````{py:attribute} CloseOutOC
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.CloseOutOC
:value: >
   2

```{autodoc2-docstring} algokit_subscriber.types.transaction.AlgodOnComplete.CloseOutOC
```

````

````{py:attribute} ClearStateOC
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.ClearStateOC
:value: >
   3

```{autodoc2-docstring} algokit_subscriber.types.transaction.AlgodOnComplete.ClearStateOC
```

````

````{py:attribute} UpdateApplicationOC
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.UpdateApplicationOC
:value: >
   4

```{autodoc2-docstring} algokit_subscriber.types.transaction.AlgodOnComplete.UpdateApplicationOC
```

````

````{py:attribute} DeleteApplicationOC
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.DeleteApplicationOC
:value: >
   5

```{autodoc2-docstring} algokit_subscriber.types.transaction.AlgodOnComplete.DeleteApplicationOC
```

````

````{py:method} __abs__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__abs__

````

````{py:method} __add__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__add__

````

````{py:method} __and__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__and__

````

````{py:method} __bool__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__bool__

````

````{py:method} __ceil__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__ceil__

````

````{py:method} __delattr__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__delattr__

````

````{py:method} __dir__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__dir__

````

````{py:method} __divmod__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__divmod__

````

````{py:method} __eq__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__eq__

````

````{py:method} __float__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__float__

````

````{py:method} __floor__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__floor__

````

````{py:method} __floordiv__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__floordiv__

````

````{py:method} __format__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__format__

````

````{py:method} __ge__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__ge__

````

````{py:method} __getattribute__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__getattribute__

````

````{py:method} __getnewargs__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__getnewargs__

````

````{py:method} __getstate__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__getstate__

````

````{py:method} __gt__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__gt__

````

````{py:method} __hash__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__hash__

````

````{py:method} __index__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__index__

````

````{py:method} __int__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__int__

````

````{py:method} __invert__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__invert__

````

````{py:method} __le__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__le__

````

````{py:method} __lshift__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__lshift__

````

````{py:method} __lt__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__lt__

````

````{py:method} __mod__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__mod__

````

````{py:method} __mul__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__mul__

````

````{py:method} __ne__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__ne__

````

````{py:method} __neg__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__neg__

````

````{py:method} __new__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__new__

````

````{py:method} __or__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__or__

````

````{py:method} __pos__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__pos__

````

````{py:method} __pow__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__pow__

````

````{py:method} __radd__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__radd__

````

````{py:method} __rand__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__rand__

````

````{py:method} __rdivmod__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__rdivmod__

````

````{py:method} __reduce__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__reduce__

````

````{py:method} __reduce_ex__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__reduce_ex__

````

````{py:method} __repr__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__repr__

````

````{py:method} __rfloordiv__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__rfloordiv__

````

````{py:method} __rlshift__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__rlshift__

````

````{py:method} __rmod__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__rmod__

````

````{py:method} __rmul__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__rmul__

````

````{py:method} __ror__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__ror__

````

````{py:method} __round__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__round__

````

````{py:method} __rpow__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__rpow__

````

````{py:method} __rrshift__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__rrshift__

````

````{py:method} __rshift__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__rshift__

````

````{py:method} __rsub__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__rsub__

````

````{py:method} __rtruediv__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__rtruediv__

````

````{py:method} __rxor__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__rxor__

````

````{py:method} __setattr__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__setattr__

````

````{py:method} __sizeof__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__sizeof__

````

````{py:method} __str__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__str__

````

````{py:method} __sub__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__sub__

````

````{py:method} __subclasshook__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__subclasshook__

````

````{py:method} __truediv__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__truediv__

````

````{py:method} __trunc__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__trunc__

````

````{py:method} __xor__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__xor__

````

````{py:method} as_integer_ratio()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.as_integer_ratio

````

````{py:method} bit_count()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.bit_count

````

````{py:method} bit_length()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.bit_length

````

````{py:method} conjugate()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.conjugate

````

```{py:class} denominator
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.denominator

```

```{py:class} imag
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.imag

```

````{py:method} is_integer()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.is_integer

````

```{py:class} numerator
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.numerator

```

```{py:class} real
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.real

```

````{py:method} to_bytes()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.to_bytes

````

````{py:method} __signature__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__signature__
:classmethod:

````

````{py:method} __deepcopy__(memo)
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__deepcopy__

````

````{py:method} __copy__()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.__copy__

````

````{py:method} name()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.name

````

````{py:method} value()
:canonical: algokit_subscriber.types.transaction.AlgodOnComplete.value

````

`````

`````{py:class} IndexerOnComplete(*args, **kwds)
:canonical: algokit_subscriber.types.transaction.IndexerOnComplete

Bases: {py:obj}`enum.Enum`

```{autodoc2-docstring} algokit_subscriber.types.transaction.IndexerOnComplete
```

```{rubric} Initialization
```

```{autodoc2-docstring} algokit_subscriber.types.transaction.IndexerOnComplete.__init__
```

````{py:attribute} noop
:canonical: algokit_subscriber.types.transaction.IndexerOnComplete.noop
:value: >
   'noop'

```{autodoc2-docstring} algokit_subscriber.types.transaction.IndexerOnComplete.noop
```

````

````{py:attribute} optin
:canonical: algokit_subscriber.types.transaction.IndexerOnComplete.optin
:value: >
   'optin'

```{autodoc2-docstring} algokit_subscriber.types.transaction.IndexerOnComplete.optin
```

````

````{py:attribute} closeout
:canonical: algokit_subscriber.types.transaction.IndexerOnComplete.closeout
:value: >
   'closeout'

```{autodoc2-docstring} algokit_subscriber.types.transaction.IndexerOnComplete.closeout
```

````

````{py:attribute} clear
:canonical: algokit_subscriber.types.transaction.IndexerOnComplete.clear
:value: >
   'clear'

```{autodoc2-docstring} algokit_subscriber.types.transaction.IndexerOnComplete.clear
```

````

````{py:attribute} update
:canonical: algokit_subscriber.types.transaction.IndexerOnComplete.update
:value: >
   'update'

```{autodoc2-docstring} algokit_subscriber.types.transaction.IndexerOnComplete.update
```

````

````{py:attribute} delete
:canonical: algokit_subscriber.types.transaction.IndexerOnComplete.delete
:value: >
   'delete'

```{autodoc2-docstring} algokit_subscriber.types.transaction.IndexerOnComplete.delete
```

````

````{py:method} __signature__()
:canonical: algokit_subscriber.types.transaction.IndexerOnComplete.__signature__
:classmethod:

````

````{py:method} __new__(value)
:canonical: algokit_subscriber.types.transaction.IndexerOnComplete.__new__

````

````{py:method} __repr__()
:canonical: algokit_subscriber.types.transaction.IndexerOnComplete.__repr__

````

````{py:method} __str__()
:canonical: algokit_subscriber.types.transaction.IndexerOnComplete.__str__

````

````{py:method} __dir__()
:canonical: algokit_subscriber.types.transaction.IndexerOnComplete.__dir__

````

````{py:method} __format__(format_spec)
:canonical: algokit_subscriber.types.transaction.IndexerOnComplete.__format__

````

````{py:method} __hash__()
:canonical: algokit_subscriber.types.transaction.IndexerOnComplete.__hash__

````

````{py:method} __reduce_ex__(proto)
:canonical: algokit_subscriber.types.transaction.IndexerOnComplete.__reduce_ex__

````

````{py:method} __deepcopy__(memo)
:canonical: algokit_subscriber.types.transaction.IndexerOnComplete.__deepcopy__

````

````{py:method} __copy__()
:canonical: algokit_subscriber.types.transaction.IndexerOnComplete.__copy__

````

````{py:method} name()
:canonical: algokit_subscriber.types.transaction.IndexerOnComplete.name

````

````{py:method} value()
:canonical: algokit_subscriber.types.transaction.IndexerOnComplete.value

````

`````
