---
title: algokit_subscriber.types.arc28
---

# [`algokit_subscriber.types.arc28`](#module-algokit_subscriber.types.arc28)

## Module Contents

### Classes

| [`Arc28EventArg`](#algokit_subscriber.types.arc28.Arc28EventArg)             | Represents an argument of an ARC-28 event.                                                                       |
|------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| [`Arc28Event`](#algokit_subscriber.types.arc28.Arc28Event)                   | The definition of metadata for an ARC-28 event as per the ARC-28 specification.                                  |
| [`Arc28EventGroup`](#algokit_subscriber.types.arc28.Arc28EventGroup)         | Specifies a group of ARC-28 event definitions along with instructions for when to attempt to process the events. |
| [`Arc28EventToProcess`](#algokit_subscriber.types.arc28.Arc28EventToProcess) | Represents an ARC-28 event to be processed.                                                                      |
| [`EmittedArc28Event`](#algokit_subscriber.types.arc28.EmittedArc28Event)     | Represents an ARC-28 event that was emitted.                                                                     |

### API

### *class* Arc28EventArg

Bases: `typing.TypedDict`

Represents an argument of an ARC-28 event.

### Initialization

Initialize self.  See help(type(self)) for accurate signature.

#### type *: str*

None

The type of the argument

#### name *: typing_extensions.NotRequired[str]*

None

An optional, user-friendly name for the argument

#### desc *: typing_extensions.NotRequired[str]*

None

An optional, user-friendly description for the argument

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

### *class* Arc28Event

Bases: `typing.TypedDict`

The definition of metadata for an ARC-28 event as per the ARC-28 specification.

### Initialization

Initialize self.  See help(type(self)) for accurate signature.

#### name *: str*

None

The name of the event

#### desc *: typing_extensions.NotRequired[str]*

None

An optional, user-friendly description for the event

#### args *: list[[algokit_subscriber.types.arc28.Arc28EventArg](#algokit_subscriber.types.arc28.Arc28EventArg)]*

None

The arguments of the event, in order

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

### *class* Arc28EventGroup

Bases: `typing.TypedDict`

Specifies a group of ARC-28 event definitions along with instructions for when to attempt to process the events.

### Initialization

Initialize self.  See help(type(self)) for accurate signature.

#### group_name *: str*

None

The name to designate for this group of events.

#### process_for_app_ids *: list[int]*

None

Optional list of app IDs that this event should apply to.

#### process_transaction *: typing_extensions.NotRequired[collections.abc.Callable[[algokit_subscriber.types.indexer.TransactionResult], bool]]*

None

Optional predicate to indicate if these ARC-28 events should be processed for the given transaction.

#### continue_on_error *: bool*

None

Whether or not to silently (with warning log) continue if an error is encountered processing the ARC-28 event data; default = False.

#### events *: list[[algokit_subscriber.types.arc28.Arc28Event](#algokit_subscriber.types.arc28.Arc28Event)]*

None

The list of ARC-28 event definitions.

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

### *class* Arc28EventToProcess

Bases: `typing.TypedDict`

Represents an ARC-28 event to be processed.

### Initialization

Initialize self.  See help(type(self)) for accurate signature.

#### group_name *: str*

None

The name of the ARC-28 event group the event belongs to

#### event_name *: str*

None

The name of the ARC-28 event that was triggered

#### event_signature *: str*

None

The signature of the event e.g. `EventName(type1,type2)`

#### event_prefix *: str*

None

The 4-byte hex prefix for the event

#### event_definition *: [algokit_subscriber.types.arc28.Arc28Event](#algokit_subscriber.types.arc28.Arc28Event)*

None

The ARC-28 definition of the event

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

### *class* EmittedArc28Event

Bases: [`algokit_subscriber.types.arc28.Arc28EventToProcess`](#algokit_subscriber.types.arc28.Arc28EventToProcess)

Represents an ARC-28 event that was emitted.

### Initialization

Initialize self.  See help(type(self)) for accurate signature.

#### args *: list[Any]*

None

The ordered arguments extracted from the event that was emitted

#### args_by_name *: dict[str, Any]*

None

The named arguments extracted from the event that was emitted (where the arguments had a name defined)

#### group_name *: str*

None

#### event_name *: str*

None

#### event_signature *: str*

None

#### event_prefix *: str*

None

#### event_definition *: [algokit_subscriber.types.arc28.Arc28Event](#algokit_subscriber.types.arc28.Arc28Event)*

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
