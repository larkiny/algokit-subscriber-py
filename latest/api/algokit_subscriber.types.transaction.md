---
title: algokit_subscriber.types.transaction
---

# [`algokit_subscriber.types.transaction`](#module-algokit_subscriber.types.transaction)

## Module Contents

### Classes

| [`TransactionType`](#algokit_subscriber.types.transaction.TransactionType)     | Enum representing different transaction types.                   |
|--------------------------------------------------------------------------------|------------------------------------------------------------------|
| [`AlgodOnComplete`](#algokit_subscriber.types.transaction.AlgodOnComplete)     | Enum representing the different types of application completion. |
| [`IndexerOnComplete`](#algokit_subscriber.types.transaction.IndexerOnComplete) | Enum representing the different types of application completion. |

### Data

| [`AnyTransaction`](#algokit_subscriber.types.transaction.AnyTransaction)   |    |
|----------------------------------------------------------------------------|----|

### API

### AnyTransaction

None

### *class* TransactionType(\*args, \*\*kwds)

Bases: `enum.Enum`

Enum representing different transaction types.

### Initialization

#### pay

‘pay’

#### keyreg

‘keyreg’

#### acfg

‘acfg’

#### axfer

‘axfer’

#### afrz

‘afrz’

#### appl

‘appl’

#### stpf

‘stpf’

#### hb

‘hb’

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

### *class* AlgodOnComplete

Bases: `enum.IntEnum`

Enum representing the different types of application completion.

### Initialization

Initialize self.  See help(type(self)) for accurate signature.

#### NoOpOC

0

NoOpOC indicates that an application transaction will simply call its
ApprovalProgram

#### OptInOC

1

OptInOC indicates that an application transaction will allocate some
LocalState for the application in the sender’s account

#### CloseOutOC

2

CloseOutOC indicates that an application transaction will deallocate
some LocalState for the application from the user’s account

#### ClearStateOC

3

ClearStateOC is similar to CloseOutOC, but may never fail. This
allows users to reclaim their minimum balance from an application
they no longer wish to opt in to.

#### UpdateApplicationOC

4

UpdateApplicationOC indicates that an application transaction will
update the ApprovalProgram and ClearStateProgram for the application

#### DeleteApplicationOC

5

DeleteApplicationOC indicates that an application transaction will
delete the AppParams for the application from the creator’s balance
record

#### \_\_abs_\_()

#### \_\_add_\_()

#### \_\_and_\_()

#### \_\_bool_\_()

#### \_\_ceil_\_()

#### \_\_delattr_\_()

#### \_\_dir_\_()

#### \_\_divmod_\_()

#### \_\_eq_\_()

#### \_\_float_\_()

#### \_\_floor_\_()

#### \_\_floordiv_\_()

#### \_\_format_\_()

#### \_\_ge_\_()

#### \_\_getattribute_\_()

#### \_\_getnewargs_\_()

#### \_\_getstate_\_()

#### \_\_gt_\_()

#### \_\_hash_\_()

#### \_\_index_\_()

#### \_\_int_\_()

#### \_\_invert_\_()

#### \_\_le_\_()

#### \_\_lshift_\_()

#### \_\_lt_\_()

#### \_\_mod_\_()

#### \_\_mul_\_()

#### \_\_ne_\_()

#### \_\_neg_\_()

#### \_\_new_\_()

#### \_\_or_\_()

#### \_\_pos_\_()

#### \_\_pow_\_()

#### \_\_radd_\_()

#### \_\_rand_\_()

#### \_\_rdivmod_\_()

#### \_\_reduce_\_()

#### \_\_reduce_ex_\_()

#### \_\_repr_\_()

#### \_\_rfloordiv_\_()

#### \_\_rlshift_\_()

#### \_\_rmod_\_()

#### \_\_rmul_\_()

#### \_\_ror_\_()

#### \_\_round_\_()

#### \_\_rpow_\_()

#### \_\_rrshift_\_()

#### \_\_rshift_\_()

#### \_\_rsub_\_()

#### \_\_rtruediv_\_()

#### \_\_rxor_\_()

#### \_\_setattr_\_()

#### \_\_sizeof_\_()

#### \_\_str_\_()

#### \_\_sub_\_()

#### \_\_subclasshook_\_()

#### \_\_truediv_\_()

#### \_\_trunc_\_()

#### \_\_xor_\_()

#### as_integer_ratio()

#### bit_count()

#### bit_length()

#### conjugate()

#### *class* denominator

#### *class* imag

#### is_integer()

#### *class* numerator

#### *class* real

#### to_bytes()

#### *classmethod* \_\_signature_\_()

#### \_\_deepcopy_\_(memo)

#### \_\_copy_\_()

#### name()

#### value()

### *class* IndexerOnComplete(\*args, \*\*kwds)

Bases: `enum.Enum`

Enum representing the different types of application completion.

### Initialization

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
