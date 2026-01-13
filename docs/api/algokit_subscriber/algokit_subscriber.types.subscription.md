# {py:mod}`algokit_subscriber.types.subscription`

```{py:module} algokit_subscriber.types.subscription
```

```{autodoc2-docstring} algokit_subscriber.types.subscription
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`BalanceChangeRole <algokit_subscriber.types.subscription.BalanceChangeRole>`
  -
* - {py:obj}`TransactionSubscriptionResult <algokit_subscriber.types.subscription.TransactionSubscriptionResult>`
  - ```{autodoc2-docstring} algokit_subscriber.types.subscription.TransactionSubscriptionResult
    :summary:
    ```
* - {py:obj}`BlockMetadata <algokit_subscriber.types.subscription.BlockMetadata>`
  - ```{autodoc2-docstring} algokit_subscriber.types.subscription.BlockMetadata
    :summary:
    ```
* - {py:obj}`BlockRewards <algokit_subscriber.types.subscription.BlockRewards>`
  -
* - {py:obj}`BlockUpgradeState <algokit_subscriber.types.subscription.BlockUpgradeState>`
  -
* - {py:obj}`SubscribedTransaction <algokit_subscriber.types.subscription.SubscribedTransaction>`
  - ```{autodoc2-docstring} algokit_subscriber.types.subscription.SubscribedTransaction
    :summary:
    ```
* - {py:obj}`BalanceChange <algokit_subscriber.types.subscription.BalanceChange>`
  - ```{autodoc2-docstring} algokit_subscriber.types.subscription.BalanceChange
    :summary:
    ```
* - {py:obj}`BeforePollMetadata <algokit_subscriber.types.subscription.BeforePollMetadata>`
  - ```{autodoc2-docstring} algokit_subscriber.types.subscription.BeforePollMetadata
    :summary:
    ```
* - {py:obj}`TransactionFilter <algokit_subscriber.types.subscription.TransactionFilter>`
  -
* - {py:obj}`NamedTransactionFilter <algokit_subscriber.types.subscription.NamedTransactionFilter>`
  - ```{autodoc2-docstring} algokit_subscriber.types.subscription.NamedTransactionFilter
    :summary:
    ```
* - {py:obj}`CoreTransactionSubscriptionParams <algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams>`
  -
* - {py:obj}`TransactionSubscriptionParams <algokit_subscriber.types.subscription.TransactionSubscriptionParams>`
  -
* - {py:obj}`WatermarkPersistence <algokit_subscriber.types.subscription.WatermarkPersistence>`
  -
* - {py:obj}`AlgorandSubscriberConfig <algokit_subscriber.types.subscription.AlgorandSubscriberConfig>`
  - ```{autodoc2-docstring} algokit_subscriber.types.subscription.AlgorandSubscriberConfig
    :summary:
    ```
* - {py:obj}`SubscriberConfigFilter <algokit_subscriber.types.subscription.SubscriberConfigFilter>`
  - ```{autodoc2-docstring} algokit_subscriber.types.subscription.SubscriberConfigFilter
    :summary:
    ```
````

### API

`````{py:class} BalanceChangeRole(*args, **kwds)
:canonical: algokit_subscriber.types.subscription.BalanceChangeRole

Bases: {py:obj}`enum.Enum`

````{py:attribute} Sender
:canonical: algokit_subscriber.types.subscription.BalanceChangeRole.Sender
:value: >
   'Sender'

```{autodoc2-docstring} algokit_subscriber.types.subscription.BalanceChangeRole.Sender
```

````

````{py:attribute} Receiver
:canonical: algokit_subscriber.types.subscription.BalanceChangeRole.Receiver
:value: >
   'Receiver'

```{autodoc2-docstring} algokit_subscriber.types.subscription.BalanceChangeRole.Receiver
```

````

````{py:attribute} CloseTo
:canonical: algokit_subscriber.types.subscription.BalanceChangeRole.CloseTo
:value: >
   'CloseTo'

```{autodoc2-docstring} algokit_subscriber.types.subscription.BalanceChangeRole.CloseTo
```

````

````{py:attribute} AssetCreator
:canonical: algokit_subscriber.types.subscription.BalanceChangeRole.AssetCreator
:value: >
   'AssetCreator'

```{autodoc2-docstring} algokit_subscriber.types.subscription.BalanceChangeRole.AssetCreator
```

````

````{py:attribute} AssetDestroyer
:canonical: algokit_subscriber.types.subscription.BalanceChangeRole.AssetDestroyer
:value: >
   'AssetDestroyer'

```{autodoc2-docstring} algokit_subscriber.types.subscription.BalanceChangeRole.AssetDestroyer
```

````

````{py:method} __signature__()
:canonical: algokit_subscriber.types.subscription.BalanceChangeRole.__signature__
:classmethod:

````

````{py:method} __new__(value)
:canonical: algokit_subscriber.types.subscription.BalanceChangeRole.__new__

````

````{py:method} __repr__()
:canonical: algokit_subscriber.types.subscription.BalanceChangeRole.__repr__

````

````{py:method} __str__()
:canonical: algokit_subscriber.types.subscription.BalanceChangeRole.__str__

````

````{py:method} __dir__()
:canonical: algokit_subscriber.types.subscription.BalanceChangeRole.__dir__

````

````{py:method} __format__(format_spec)
:canonical: algokit_subscriber.types.subscription.BalanceChangeRole.__format__

````

````{py:method} __hash__()
:canonical: algokit_subscriber.types.subscription.BalanceChangeRole.__hash__

````

````{py:method} __reduce_ex__(proto)
:canonical: algokit_subscriber.types.subscription.BalanceChangeRole.__reduce_ex__

````

````{py:method} __deepcopy__(memo)
:canonical: algokit_subscriber.types.subscription.BalanceChangeRole.__deepcopy__

````

````{py:method} __copy__()
:canonical: algokit_subscriber.types.subscription.BalanceChangeRole.__copy__

````

````{py:method} name()
:canonical: algokit_subscriber.types.subscription.BalanceChangeRole.name

````

````{py:method} value()
:canonical: algokit_subscriber.types.subscription.BalanceChangeRole.value

````

`````

`````{py:class} TransactionSubscriptionResult()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionResult

Bases: {py:obj}`typing.TypedDict`

```{autodoc2-docstring} algokit_subscriber.types.subscription.TransactionSubscriptionResult
```

```{rubric} Initialization
```

```{autodoc2-docstring} algokit_subscriber.types.subscription.TransactionSubscriptionResult.__init__
```

````{py:attribute} synced_round_range
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionResult.synced_round_range
:type: tuple[int, int]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.TransactionSubscriptionResult.synced_round_range
```

````

````{py:attribute} current_round
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionResult.current_round
:type: int
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.TransactionSubscriptionResult.current_round
```

````

````{py:attribute} starting_watermark
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionResult.starting_watermark
:type: int
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.TransactionSubscriptionResult.starting_watermark
```

````

````{py:attribute} new_watermark
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionResult.new_watermark
:type: int
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.TransactionSubscriptionResult.new_watermark
```

````

````{py:attribute} subscribed_transactions
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionResult.subscribed_transactions
:type: list[SubscribedTransaction]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.TransactionSubscriptionResult.subscribed_transactions
```

````

````{py:attribute} block_metadata
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionResult.block_metadata
:type: typing_extensions.NotRequired[list[BlockMetadata]]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.TransactionSubscriptionResult.block_metadata
```

````

````{py:method} __contains__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionResult.__contains__

````

````{py:method} __delattr__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionResult.__delattr__

````

````{py:method} __delitem__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionResult.__delitem__

````

````{py:method} __dir__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionResult.__dir__

````

````{py:method} __eq__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionResult.__eq__

````

````{py:method} __format__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionResult.__format__

````

````{py:method} __ge__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionResult.__ge__

````

````{py:method} __getattribute__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionResult.__getattribute__

````

````{py:method} __getitem__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionResult.__getitem__

````

````{py:method} __getstate__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionResult.__getstate__

````

````{py:method} __gt__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionResult.__gt__

````

````{py:method} __ior__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionResult.__ior__

````

````{py:method} __iter__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionResult.__iter__

````

````{py:method} __le__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionResult.__le__

````

````{py:method} __len__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionResult.__len__

````

````{py:method} __lt__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionResult.__lt__

````

````{py:method} __ne__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionResult.__ne__

````

````{py:method} __new__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionResult.__new__

````

````{py:method} __or__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionResult.__or__

````

````{py:method} __reduce__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionResult.__reduce__

````

````{py:method} __reduce_ex__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionResult.__reduce_ex__

````

````{py:method} __repr__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionResult.__repr__

````

````{py:method} __reversed__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionResult.__reversed__

````

````{py:method} __ror__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionResult.__ror__

````

````{py:method} __setattr__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionResult.__setattr__

````

````{py:method} __setitem__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionResult.__setitem__

````

````{py:method} __sizeof__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionResult.__sizeof__

````

````{py:method} __str__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionResult.__str__

````

````{py:method} __subclasshook__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionResult.__subclasshook__

````

````{py:method} clear()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionResult.clear

````

````{py:method} copy()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionResult.copy

````

````{py:method} get()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionResult.get

````

````{py:method} items()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionResult.items

````

````{py:method} keys()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionResult.keys

````

````{py:method} pop()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionResult.pop

````

````{py:method} popitem()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionResult.popitem

````

````{py:method} setdefault()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionResult.setdefault

````

````{py:method} update()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionResult.update

````

````{py:method} values()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionResult.values

````

`````

`````{py:class} BlockMetadata()
:canonical: algokit_subscriber.types.subscription.BlockMetadata

Bases: {py:obj}`typing.TypedDict`

```{autodoc2-docstring} algokit_subscriber.types.subscription.BlockMetadata
```

```{rubric} Initialization
```

```{autodoc2-docstring} algokit_subscriber.types.subscription.BlockMetadata.__init__
```

````{py:attribute} hash
:canonical: algokit_subscriber.types.subscription.BlockMetadata.hash
:type: typing_extensions.NotRequired[str | None]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.BlockMetadata.hash
```

````

````{py:attribute} round
:canonical: algokit_subscriber.types.subscription.BlockMetadata.round
:type: int
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.BlockMetadata.round
```

````

````{py:attribute} timestamp
:canonical: algokit_subscriber.types.subscription.BlockMetadata.timestamp
:type: int
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.BlockMetadata.timestamp
```

````

````{py:attribute} genesis_id
:canonical: algokit_subscriber.types.subscription.BlockMetadata.genesis_id
:type: str
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.BlockMetadata.genesis_id
```

````

````{py:attribute} genesis_hash
:canonical: algokit_subscriber.types.subscription.BlockMetadata.genesis_hash
:type: str
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.BlockMetadata.genesis_hash
```

````

````{py:attribute} previous_block_hash
:canonical: algokit_subscriber.types.subscription.BlockMetadata.previous_block_hash
:type: typing_extensions.NotRequired[str | None]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.BlockMetadata.previous_block_hash
```

````

````{py:attribute} seed
:canonical: algokit_subscriber.types.subscription.BlockMetadata.seed
:type: str
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.BlockMetadata.seed
```

````

````{py:attribute} rewards
:canonical: algokit_subscriber.types.subscription.BlockMetadata.rewards
:type: typing_extensions.NotRequired[BlockRewards]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.BlockMetadata.rewards
```

````

````{py:attribute} parent_transaction_count
:canonical: algokit_subscriber.types.subscription.BlockMetadata.parent_transaction_count
:type: int
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.BlockMetadata.parent_transaction_count
```

````

````{py:attribute} full_transaction_count
:canonical: algokit_subscriber.types.subscription.BlockMetadata.full_transaction_count
:type: int
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.BlockMetadata.full_transaction_count
```

````

````{py:attribute} txn_counter
:canonical: algokit_subscriber.types.subscription.BlockMetadata.txn_counter
:type: int
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.BlockMetadata.txn_counter
```

````

````{py:attribute} transactions_root
:canonical: algokit_subscriber.types.subscription.BlockMetadata.transactions_root
:type: str
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.BlockMetadata.transactions_root
```

````

````{py:attribute} transactions_root_sha256
:canonical: algokit_subscriber.types.subscription.BlockMetadata.transactions_root_sha256
:type: str
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.BlockMetadata.transactions_root_sha256
```

````

````{py:attribute} upgrade_state
:canonical: algokit_subscriber.types.subscription.BlockMetadata.upgrade_state
:type: typing_extensions.NotRequired[BlockUpgradeState]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.BlockMetadata.upgrade_state
```

````

````{py:method} __contains__()
:canonical: algokit_subscriber.types.subscription.BlockMetadata.__contains__

````

````{py:method} __delattr__()
:canonical: algokit_subscriber.types.subscription.BlockMetadata.__delattr__

````

````{py:method} __delitem__()
:canonical: algokit_subscriber.types.subscription.BlockMetadata.__delitem__

````

````{py:method} __dir__()
:canonical: algokit_subscriber.types.subscription.BlockMetadata.__dir__

````

````{py:method} __eq__()
:canonical: algokit_subscriber.types.subscription.BlockMetadata.__eq__

````

````{py:method} __format__()
:canonical: algokit_subscriber.types.subscription.BlockMetadata.__format__

````

````{py:method} __ge__()
:canonical: algokit_subscriber.types.subscription.BlockMetadata.__ge__

````

````{py:method} __getattribute__()
:canonical: algokit_subscriber.types.subscription.BlockMetadata.__getattribute__

````

````{py:method} __getitem__()
:canonical: algokit_subscriber.types.subscription.BlockMetadata.__getitem__

````

````{py:method} __getstate__()
:canonical: algokit_subscriber.types.subscription.BlockMetadata.__getstate__

````

````{py:method} __gt__()
:canonical: algokit_subscriber.types.subscription.BlockMetadata.__gt__

````

````{py:method} __ior__()
:canonical: algokit_subscriber.types.subscription.BlockMetadata.__ior__

````

````{py:method} __iter__()
:canonical: algokit_subscriber.types.subscription.BlockMetadata.__iter__

````

````{py:method} __le__()
:canonical: algokit_subscriber.types.subscription.BlockMetadata.__le__

````

````{py:method} __len__()
:canonical: algokit_subscriber.types.subscription.BlockMetadata.__len__

````

````{py:method} __lt__()
:canonical: algokit_subscriber.types.subscription.BlockMetadata.__lt__

````

````{py:method} __ne__()
:canonical: algokit_subscriber.types.subscription.BlockMetadata.__ne__

````

````{py:method} __new__()
:canonical: algokit_subscriber.types.subscription.BlockMetadata.__new__

````

````{py:method} __or__()
:canonical: algokit_subscriber.types.subscription.BlockMetadata.__or__

````

````{py:method} __reduce__()
:canonical: algokit_subscriber.types.subscription.BlockMetadata.__reduce__

````

````{py:method} __reduce_ex__()
:canonical: algokit_subscriber.types.subscription.BlockMetadata.__reduce_ex__

````

````{py:method} __repr__()
:canonical: algokit_subscriber.types.subscription.BlockMetadata.__repr__

````

````{py:method} __reversed__()
:canonical: algokit_subscriber.types.subscription.BlockMetadata.__reversed__

````

````{py:method} __ror__()
:canonical: algokit_subscriber.types.subscription.BlockMetadata.__ror__

````

````{py:method} __setattr__()
:canonical: algokit_subscriber.types.subscription.BlockMetadata.__setattr__

````

````{py:method} __setitem__()
:canonical: algokit_subscriber.types.subscription.BlockMetadata.__setitem__

````

````{py:method} __sizeof__()
:canonical: algokit_subscriber.types.subscription.BlockMetadata.__sizeof__

````

````{py:method} __str__()
:canonical: algokit_subscriber.types.subscription.BlockMetadata.__str__

````

````{py:method} __subclasshook__()
:canonical: algokit_subscriber.types.subscription.BlockMetadata.__subclasshook__

````

````{py:method} clear()
:canonical: algokit_subscriber.types.subscription.BlockMetadata.clear

````

````{py:method} copy()
:canonical: algokit_subscriber.types.subscription.BlockMetadata.copy

````

````{py:method} get()
:canonical: algokit_subscriber.types.subscription.BlockMetadata.get

````

````{py:method} items()
:canonical: algokit_subscriber.types.subscription.BlockMetadata.items

````

````{py:method} keys()
:canonical: algokit_subscriber.types.subscription.BlockMetadata.keys

````

````{py:method} pop()
:canonical: algokit_subscriber.types.subscription.BlockMetadata.pop

````

````{py:method} popitem()
:canonical: algokit_subscriber.types.subscription.BlockMetadata.popitem

````

````{py:method} setdefault()
:canonical: algokit_subscriber.types.subscription.BlockMetadata.setdefault

````

````{py:method} update()
:canonical: algokit_subscriber.types.subscription.BlockMetadata.update

````

````{py:method} values()
:canonical: algokit_subscriber.types.subscription.BlockMetadata.values

````

`````

`````{py:class} BlockRewards()
:canonical: algokit_subscriber.types.subscription.BlockRewards

Bases: {py:obj}`typing.TypedDict`

````{py:attribute} fee_sink
:canonical: algokit_subscriber.types.subscription.BlockRewards.fee_sink
:type: str
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.BlockRewards.fee_sink
```

````

````{py:attribute} rewards_calculation_round
:canonical: algokit_subscriber.types.subscription.BlockRewards.rewards_calculation_round
:type: int
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.BlockRewards.rewards_calculation_round
```

````

````{py:attribute} rewards_level
:canonical: algokit_subscriber.types.subscription.BlockRewards.rewards_level
:type: int
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.BlockRewards.rewards_level
```

````

````{py:attribute} rewards_pool
:canonical: algokit_subscriber.types.subscription.BlockRewards.rewards_pool
:type: str
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.BlockRewards.rewards_pool
```

````

````{py:attribute} rewards_rate
:canonical: algokit_subscriber.types.subscription.BlockRewards.rewards_rate
:type: int
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.BlockRewards.rewards_rate
```

````

````{py:attribute} rewards_residue
:canonical: algokit_subscriber.types.subscription.BlockRewards.rewards_residue
:type: int
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.BlockRewards.rewards_residue
```

````

````{py:method} __contains__()
:canonical: algokit_subscriber.types.subscription.BlockRewards.__contains__

````

````{py:method} __delattr__()
:canonical: algokit_subscriber.types.subscription.BlockRewards.__delattr__

````

````{py:method} __delitem__()
:canonical: algokit_subscriber.types.subscription.BlockRewards.__delitem__

````

````{py:method} __dir__()
:canonical: algokit_subscriber.types.subscription.BlockRewards.__dir__

````

````{py:method} __eq__()
:canonical: algokit_subscriber.types.subscription.BlockRewards.__eq__

````

````{py:method} __format__()
:canonical: algokit_subscriber.types.subscription.BlockRewards.__format__

````

````{py:method} __ge__()
:canonical: algokit_subscriber.types.subscription.BlockRewards.__ge__

````

````{py:method} __getattribute__()
:canonical: algokit_subscriber.types.subscription.BlockRewards.__getattribute__

````

````{py:method} __getitem__()
:canonical: algokit_subscriber.types.subscription.BlockRewards.__getitem__

````

````{py:method} __getstate__()
:canonical: algokit_subscriber.types.subscription.BlockRewards.__getstate__

````

````{py:method} __gt__()
:canonical: algokit_subscriber.types.subscription.BlockRewards.__gt__

````

````{py:method} __ior__()
:canonical: algokit_subscriber.types.subscription.BlockRewards.__ior__

````

````{py:method} __iter__()
:canonical: algokit_subscriber.types.subscription.BlockRewards.__iter__

````

````{py:method} __le__()
:canonical: algokit_subscriber.types.subscription.BlockRewards.__le__

````

````{py:method} __len__()
:canonical: algokit_subscriber.types.subscription.BlockRewards.__len__

````

````{py:method} __lt__()
:canonical: algokit_subscriber.types.subscription.BlockRewards.__lt__

````

````{py:method} __ne__()
:canonical: algokit_subscriber.types.subscription.BlockRewards.__ne__

````

````{py:method} __new__()
:canonical: algokit_subscriber.types.subscription.BlockRewards.__new__

````

````{py:method} __or__()
:canonical: algokit_subscriber.types.subscription.BlockRewards.__or__

````

````{py:method} __reduce__()
:canonical: algokit_subscriber.types.subscription.BlockRewards.__reduce__

````

````{py:method} __reduce_ex__()
:canonical: algokit_subscriber.types.subscription.BlockRewards.__reduce_ex__

````

````{py:method} __repr__()
:canonical: algokit_subscriber.types.subscription.BlockRewards.__repr__

````

````{py:method} __reversed__()
:canonical: algokit_subscriber.types.subscription.BlockRewards.__reversed__

````

````{py:method} __ror__()
:canonical: algokit_subscriber.types.subscription.BlockRewards.__ror__

````

````{py:method} __setattr__()
:canonical: algokit_subscriber.types.subscription.BlockRewards.__setattr__

````

````{py:method} __setitem__()
:canonical: algokit_subscriber.types.subscription.BlockRewards.__setitem__

````

````{py:method} __sizeof__()
:canonical: algokit_subscriber.types.subscription.BlockRewards.__sizeof__

````

````{py:method} __str__()
:canonical: algokit_subscriber.types.subscription.BlockRewards.__str__

````

````{py:method} __subclasshook__()
:canonical: algokit_subscriber.types.subscription.BlockRewards.__subclasshook__

````

````{py:method} clear()
:canonical: algokit_subscriber.types.subscription.BlockRewards.clear

````

````{py:method} copy()
:canonical: algokit_subscriber.types.subscription.BlockRewards.copy

````

````{py:method} get()
:canonical: algokit_subscriber.types.subscription.BlockRewards.get

````

````{py:method} items()
:canonical: algokit_subscriber.types.subscription.BlockRewards.items

````

````{py:method} keys()
:canonical: algokit_subscriber.types.subscription.BlockRewards.keys

````

````{py:method} pop()
:canonical: algokit_subscriber.types.subscription.BlockRewards.pop

````

````{py:method} popitem()
:canonical: algokit_subscriber.types.subscription.BlockRewards.popitem

````

````{py:method} setdefault()
:canonical: algokit_subscriber.types.subscription.BlockRewards.setdefault

````

````{py:method} update()
:canonical: algokit_subscriber.types.subscription.BlockRewards.update

````

````{py:method} values()
:canonical: algokit_subscriber.types.subscription.BlockRewards.values

````

`````

`````{py:class} BlockUpgradeState()
:canonical: algokit_subscriber.types.subscription.BlockUpgradeState

Bases: {py:obj}`typing.TypedDict`

````{py:attribute} current_protocol
:canonical: algokit_subscriber.types.subscription.BlockUpgradeState.current_protocol
:type: str
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.BlockUpgradeState.current_protocol
```

````

````{py:attribute} next_protocol
:canonical: algokit_subscriber.types.subscription.BlockUpgradeState.next_protocol
:type: typing_extensions.NotRequired[None | str]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.BlockUpgradeState.next_protocol
```

````

````{py:attribute} next_protocol_approvals
:canonical: algokit_subscriber.types.subscription.BlockUpgradeState.next_protocol_approvals
:type: typing_extensions.NotRequired[None | int]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.BlockUpgradeState.next_protocol_approvals
```

````

````{py:attribute} next_protocol_vote_before
:canonical: algokit_subscriber.types.subscription.BlockUpgradeState.next_protocol_vote_before
:type: typing_extensions.NotRequired[None | int]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.BlockUpgradeState.next_protocol_vote_before
```

````

````{py:attribute} next_protocol_switch_on
:canonical: algokit_subscriber.types.subscription.BlockUpgradeState.next_protocol_switch_on
:type: typing_extensions.NotRequired[None | int]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.BlockUpgradeState.next_protocol_switch_on
```

````

````{py:method} __contains__()
:canonical: algokit_subscriber.types.subscription.BlockUpgradeState.__contains__

````

````{py:method} __delattr__()
:canonical: algokit_subscriber.types.subscription.BlockUpgradeState.__delattr__

````

````{py:method} __delitem__()
:canonical: algokit_subscriber.types.subscription.BlockUpgradeState.__delitem__

````

````{py:method} __dir__()
:canonical: algokit_subscriber.types.subscription.BlockUpgradeState.__dir__

````

````{py:method} __eq__()
:canonical: algokit_subscriber.types.subscription.BlockUpgradeState.__eq__

````

````{py:method} __format__()
:canonical: algokit_subscriber.types.subscription.BlockUpgradeState.__format__

````

````{py:method} __ge__()
:canonical: algokit_subscriber.types.subscription.BlockUpgradeState.__ge__

````

````{py:method} __getattribute__()
:canonical: algokit_subscriber.types.subscription.BlockUpgradeState.__getattribute__

````

````{py:method} __getitem__()
:canonical: algokit_subscriber.types.subscription.BlockUpgradeState.__getitem__

````

````{py:method} __getstate__()
:canonical: algokit_subscriber.types.subscription.BlockUpgradeState.__getstate__

````

````{py:method} __gt__()
:canonical: algokit_subscriber.types.subscription.BlockUpgradeState.__gt__

````

````{py:method} __ior__()
:canonical: algokit_subscriber.types.subscription.BlockUpgradeState.__ior__

````

````{py:method} __iter__()
:canonical: algokit_subscriber.types.subscription.BlockUpgradeState.__iter__

````

````{py:method} __le__()
:canonical: algokit_subscriber.types.subscription.BlockUpgradeState.__le__

````

````{py:method} __len__()
:canonical: algokit_subscriber.types.subscription.BlockUpgradeState.__len__

````

````{py:method} __lt__()
:canonical: algokit_subscriber.types.subscription.BlockUpgradeState.__lt__

````

````{py:method} __ne__()
:canonical: algokit_subscriber.types.subscription.BlockUpgradeState.__ne__

````

````{py:method} __new__()
:canonical: algokit_subscriber.types.subscription.BlockUpgradeState.__new__

````

````{py:method} __or__()
:canonical: algokit_subscriber.types.subscription.BlockUpgradeState.__or__

````

````{py:method} __reduce__()
:canonical: algokit_subscriber.types.subscription.BlockUpgradeState.__reduce__

````

````{py:method} __reduce_ex__()
:canonical: algokit_subscriber.types.subscription.BlockUpgradeState.__reduce_ex__

````

````{py:method} __repr__()
:canonical: algokit_subscriber.types.subscription.BlockUpgradeState.__repr__

````

````{py:method} __reversed__()
:canonical: algokit_subscriber.types.subscription.BlockUpgradeState.__reversed__

````

````{py:method} __ror__()
:canonical: algokit_subscriber.types.subscription.BlockUpgradeState.__ror__

````

````{py:method} __setattr__()
:canonical: algokit_subscriber.types.subscription.BlockUpgradeState.__setattr__

````

````{py:method} __setitem__()
:canonical: algokit_subscriber.types.subscription.BlockUpgradeState.__setitem__

````

````{py:method} __sizeof__()
:canonical: algokit_subscriber.types.subscription.BlockUpgradeState.__sizeof__

````

````{py:method} __str__()
:canonical: algokit_subscriber.types.subscription.BlockUpgradeState.__str__

````

````{py:method} __subclasshook__()
:canonical: algokit_subscriber.types.subscription.BlockUpgradeState.__subclasshook__

````

````{py:method} clear()
:canonical: algokit_subscriber.types.subscription.BlockUpgradeState.clear

````

````{py:method} copy()
:canonical: algokit_subscriber.types.subscription.BlockUpgradeState.copy

````

````{py:method} get()
:canonical: algokit_subscriber.types.subscription.BlockUpgradeState.get

````

````{py:method} items()
:canonical: algokit_subscriber.types.subscription.BlockUpgradeState.items

````

````{py:method} keys()
:canonical: algokit_subscriber.types.subscription.BlockUpgradeState.keys

````

````{py:method} pop()
:canonical: algokit_subscriber.types.subscription.BlockUpgradeState.pop

````

````{py:method} popitem()
:canonical: algokit_subscriber.types.subscription.BlockUpgradeState.popitem

````

````{py:method} setdefault()
:canonical: algokit_subscriber.types.subscription.BlockUpgradeState.setdefault

````

````{py:method} update()
:canonical: algokit_subscriber.types.subscription.BlockUpgradeState.update

````

````{py:method} values()
:canonical: algokit_subscriber.types.subscription.BlockUpgradeState.values

````

`````

`````{py:class} SubscribedTransaction
:canonical: algokit_subscriber.types.subscription.SubscribedTransaction

Bases: {py:obj}`algokit_subscriber.types.indexer.TransactionResult`

```{autodoc2-docstring} algokit_subscriber.types.subscription.SubscribedTransaction
```

````{py:attribute} parent_transaction_id
:canonical: algokit_subscriber.types.subscription.SubscribedTransaction.parent_transaction_id
:type: typing_extensions.NotRequired[None | str]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.SubscribedTransaction.parent_transaction_id
```

````

````{py:attribute} inner_txns
:canonical: algokit_subscriber.types.subscription.SubscribedTransaction.inner_txns
:type: typing_extensions.NotRequired[list[algokit_subscriber.types.subscription.SubscribedTransaction]]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.SubscribedTransaction.inner_txns
```

````

````{py:attribute} arc28_events
:canonical: algokit_subscriber.types.subscription.SubscribedTransaction.arc28_events
:type: typing_extensions.NotRequired[list[algokit_subscriber.types.arc28.EmittedArc28Event]]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.SubscribedTransaction.arc28_events
```

````

````{py:attribute} filters_matched
:canonical: algokit_subscriber.types.subscription.SubscribedTransaction.filters_matched
:type: typing_extensions.NotRequired[list[str]]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.SubscribedTransaction.filters_matched
```

````

````{py:attribute} balance_changes
:canonical: algokit_subscriber.types.subscription.SubscribedTransaction.balance_changes
:type: typing_extensions.NotRequired[list[BalanceChange]]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.SubscribedTransaction.balance_changes
```

````

`````

`````{py:class} BalanceChange()
:canonical: algokit_subscriber.types.subscription.BalanceChange

Bases: {py:obj}`typing.TypedDict`

```{autodoc2-docstring} algokit_subscriber.types.subscription.BalanceChange
```

```{rubric} Initialization
```

```{autodoc2-docstring} algokit_subscriber.types.subscription.BalanceChange.__init__
```

````{py:attribute} address
:canonical: algokit_subscriber.types.subscription.BalanceChange.address
:type: str
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.BalanceChange.address
```

````

````{py:attribute} asset_id
:canonical: algokit_subscriber.types.subscription.BalanceChange.asset_id
:type: int
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.BalanceChange.asset_id
```

````

````{py:attribute} amount
:canonical: algokit_subscriber.types.subscription.BalanceChange.amount
:type: int
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.BalanceChange.amount
```

````

````{py:attribute} roles
:canonical: algokit_subscriber.types.subscription.BalanceChange.roles
:type: list[algokit_subscriber.types.subscription.BalanceChangeRole]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.BalanceChange.roles
```

````

````{py:method} __contains__()
:canonical: algokit_subscriber.types.subscription.BalanceChange.__contains__

````

````{py:method} __delattr__()
:canonical: algokit_subscriber.types.subscription.BalanceChange.__delattr__

````

````{py:method} __delitem__()
:canonical: algokit_subscriber.types.subscription.BalanceChange.__delitem__

````

````{py:method} __dir__()
:canonical: algokit_subscriber.types.subscription.BalanceChange.__dir__

````

````{py:method} __eq__()
:canonical: algokit_subscriber.types.subscription.BalanceChange.__eq__

````

````{py:method} __format__()
:canonical: algokit_subscriber.types.subscription.BalanceChange.__format__

````

````{py:method} __ge__()
:canonical: algokit_subscriber.types.subscription.BalanceChange.__ge__

````

````{py:method} __getattribute__()
:canonical: algokit_subscriber.types.subscription.BalanceChange.__getattribute__

````

````{py:method} __getitem__()
:canonical: algokit_subscriber.types.subscription.BalanceChange.__getitem__

````

````{py:method} __getstate__()
:canonical: algokit_subscriber.types.subscription.BalanceChange.__getstate__

````

````{py:method} __gt__()
:canonical: algokit_subscriber.types.subscription.BalanceChange.__gt__

````

````{py:method} __ior__()
:canonical: algokit_subscriber.types.subscription.BalanceChange.__ior__

````

````{py:method} __iter__()
:canonical: algokit_subscriber.types.subscription.BalanceChange.__iter__

````

````{py:method} __le__()
:canonical: algokit_subscriber.types.subscription.BalanceChange.__le__

````

````{py:method} __len__()
:canonical: algokit_subscriber.types.subscription.BalanceChange.__len__

````

````{py:method} __lt__()
:canonical: algokit_subscriber.types.subscription.BalanceChange.__lt__

````

````{py:method} __ne__()
:canonical: algokit_subscriber.types.subscription.BalanceChange.__ne__

````

````{py:method} __new__()
:canonical: algokit_subscriber.types.subscription.BalanceChange.__new__

````

````{py:method} __or__()
:canonical: algokit_subscriber.types.subscription.BalanceChange.__or__

````

````{py:method} __reduce__()
:canonical: algokit_subscriber.types.subscription.BalanceChange.__reduce__

````

````{py:method} __reduce_ex__()
:canonical: algokit_subscriber.types.subscription.BalanceChange.__reduce_ex__

````

````{py:method} __repr__()
:canonical: algokit_subscriber.types.subscription.BalanceChange.__repr__

````

````{py:method} __reversed__()
:canonical: algokit_subscriber.types.subscription.BalanceChange.__reversed__

````

````{py:method} __ror__()
:canonical: algokit_subscriber.types.subscription.BalanceChange.__ror__

````

````{py:method} __setattr__()
:canonical: algokit_subscriber.types.subscription.BalanceChange.__setattr__

````

````{py:method} __setitem__()
:canonical: algokit_subscriber.types.subscription.BalanceChange.__setitem__

````

````{py:method} __sizeof__()
:canonical: algokit_subscriber.types.subscription.BalanceChange.__sizeof__

````

````{py:method} __str__()
:canonical: algokit_subscriber.types.subscription.BalanceChange.__str__

````

````{py:method} __subclasshook__()
:canonical: algokit_subscriber.types.subscription.BalanceChange.__subclasshook__

````

````{py:method} clear()
:canonical: algokit_subscriber.types.subscription.BalanceChange.clear

````

````{py:method} copy()
:canonical: algokit_subscriber.types.subscription.BalanceChange.copy

````

````{py:method} get()
:canonical: algokit_subscriber.types.subscription.BalanceChange.get

````

````{py:method} items()
:canonical: algokit_subscriber.types.subscription.BalanceChange.items

````

````{py:method} keys()
:canonical: algokit_subscriber.types.subscription.BalanceChange.keys

````

````{py:method} pop()
:canonical: algokit_subscriber.types.subscription.BalanceChange.pop

````

````{py:method} popitem()
:canonical: algokit_subscriber.types.subscription.BalanceChange.popitem

````

````{py:method} setdefault()
:canonical: algokit_subscriber.types.subscription.BalanceChange.setdefault

````

````{py:method} update()
:canonical: algokit_subscriber.types.subscription.BalanceChange.update

````

````{py:method} values()
:canonical: algokit_subscriber.types.subscription.BalanceChange.values

````

`````

`````{py:class} BeforePollMetadata()
:canonical: algokit_subscriber.types.subscription.BeforePollMetadata

Bases: {py:obj}`typing.TypedDict`

```{autodoc2-docstring} algokit_subscriber.types.subscription.BeforePollMetadata
```

```{rubric} Initialization
```

```{autodoc2-docstring} algokit_subscriber.types.subscription.BeforePollMetadata.__init__
```

````{py:attribute} watermark
:canonical: algokit_subscriber.types.subscription.BeforePollMetadata.watermark
:type: int
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.BeforePollMetadata.watermark
```

````

````{py:attribute} current_round
:canonical: algokit_subscriber.types.subscription.BeforePollMetadata.current_round
:type: int
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.BeforePollMetadata.current_round
```

````

````{py:method} __contains__()
:canonical: algokit_subscriber.types.subscription.BeforePollMetadata.__contains__

````

````{py:method} __delattr__()
:canonical: algokit_subscriber.types.subscription.BeforePollMetadata.__delattr__

````

````{py:method} __delitem__()
:canonical: algokit_subscriber.types.subscription.BeforePollMetadata.__delitem__

````

````{py:method} __dir__()
:canonical: algokit_subscriber.types.subscription.BeforePollMetadata.__dir__

````

````{py:method} __eq__()
:canonical: algokit_subscriber.types.subscription.BeforePollMetadata.__eq__

````

````{py:method} __format__()
:canonical: algokit_subscriber.types.subscription.BeforePollMetadata.__format__

````

````{py:method} __ge__()
:canonical: algokit_subscriber.types.subscription.BeforePollMetadata.__ge__

````

````{py:method} __getattribute__()
:canonical: algokit_subscriber.types.subscription.BeforePollMetadata.__getattribute__

````

````{py:method} __getitem__()
:canonical: algokit_subscriber.types.subscription.BeforePollMetadata.__getitem__

````

````{py:method} __getstate__()
:canonical: algokit_subscriber.types.subscription.BeforePollMetadata.__getstate__

````

````{py:method} __gt__()
:canonical: algokit_subscriber.types.subscription.BeforePollMetadata.__gt__

````

````{py:method} __ior__()
:canonical: algokit_subscriber.types.subscription.BeforePollMetadata.__ior__

````

````{py:method} __iter__()
:canonical: algokit_subscriber.types.subscription.BeforePollMetadata.__iter__

````

````{py:method} __le__()
:canonical: algokit_subscriber.types.subscription.BeforePollMetadata.__le__

````

````{py:method} __len__()
:canonical: algokit_subscriber.types.subscription.BeforePollMetadata.__len__

````

````{py:method} __lt__()
:canonical: algokit_subscriber.types.subscription.BeforePollMetadata.__lt__

````

````{py:method} __ne__()
:canonical: algokit_subscriber.types.subscription.BeforePollMetadata.__ne__

````

````{py:method} __new__()
:canonical: algokit_subscriber.types.subscription.BeforePollMetadata.__new__

````

````{py:method} __or__()
:canonical: algokit_subscriber.types.subscription.BeforePollMetadata.__or__

````

````{py:method} __reduce__()
:canonical: algokit_subscriber.types.subscription.BeforePollMetadata.__reduce__

````

````{py:method} __reduce_ex__()
:canonical: algokit_subscriber.types.subscription.BeforePollMetadata.__reduce_ex__

````

````{py:method} __repr__()
:canonical: algokit_subscriber.types.subscription.BeforePollMetadata.__repr__

````

````{py:method} __reversed__()
:canonical: algokit_subscriber.types.subscription.BeforePollMetadata.__reversed__

````

````{py:method} __ror__()
:canonical: algokit_subscriber.types.subscription.BeforePollMetadata.__ror__

````

````{py:method} __setattr__()
:canonical: algokit_subscriber.types.subscription.BeforePollMetadata.__setattr__

````

````{py:method} __setitem__()
:canonical: algokit_subscriber.types.subscription.BeforePollMetadata.__setitem__

````

````{py:method} __sizeof__()
:canonical: algokit_subscriber.types.subscription.BeforePollMetadata.__sizeof__

````

````{py:method} __str__()
:canonical: algokit_subscriber.types.subscription.BeforePollMetadata.__str__

````

````{py:method} __subclasshook__()
:canonical: algokit_subscriber.types.subscription.BeforePollMetadata.__subclasshook__

````

````{py:method} clear()
:canonical: algokit_subscriber.types.subscription.BeforePollMetadata.clear

````

````{py:method} copy()
:canonical: algokit_subscriber.types.subscription.BeforePollMetadata.copy

````

````{py:method} get()
:canonical: algokit_subscriber.types.subscription.BeforePollMetadata.get

````

````{py:method} items()
:canonical: algokit_subscriber.types.subscription.BeforePollMetadata.items

````

````{py:method} keys()
:canonical: algokit_subscriber.types.subscription.BeforePollMetadata.keys

````

````{py:method} pop()
:canonical: algokit_subscriber.types.subscription.BeforePollMetadata.pop

````

````{py:method} popitem()
:canonical: algokit_subscriber.types.subscription.BeforePollMetadata.popitem

````

````{py:method} setdefault()
:canonical: algokit_subscriber.types.subscription.BeforePollMetadata.setdefault

````

````{py:method} update()
:canonical: algokit_subscriber.types.subscription.BeforePollMetadata.update

````

````{py:method} values()
:canonical: algokit_subscriber.types.subscription.BeforePollMetadata.values

````

`````

`````{py:class} TransactionFilter()
:canonical: algokit_subscriber.types.subscription.TransactionFilter

Bases: {py:obj}`typing.TypedDict`

````{py:attribute} type
:canonical: algokit_subscriber.types.subscription.TransactionFilter.type
:type: typing_extensions.NotRequired[str | list[str]]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.TransactionFilter.type
```

````

````{py:attribute} sender
:canonical: algokit_subscriber.types.subscription.TransactionFilter.sender
:type: typing_extensions.NotRequired[str | list[str]]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.TransactionFilter.sender
```

````

````{py:attribute} receiver
:canonical: algokit_subscriber.types.subscription.TransactionFilter.receiver
:type: typing_extensions.NotRequired[str | list[str]]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.TransactionFilter.receiver
```

````

````{py:attribute} note_prefix
:canonical: algokit_subscriber.types.subscription.TransactionFilter.note_prefix
:type: typing_extensions.NotRequired[str | bytes]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.TransactionFilter.note_prefix
```

````

````{py:attribute} app_id
:canonical: algokit_subscriber.types.subscription.TransactionFilter.app_id
:type: typing_extensions.NotRequired[int | list[int]]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.TransactionFilter.app_id
```

````

````{py:attribute} app_create
:canonical: algokit_subscriber.types.subscription.TransactionFilter.app_create
:type: typing_extensions.NotRequired[bool]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.TransactionFilter.app_create
```

````

````{py:attribute} app_on_complete
:canonical: algokit_subscriber.types.subscription.TransactionFilter.app_on_complete
:type: typing_extensions.NotRequired[str | list[str]]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.TransactionFilter.app_on_complete
```

````

````{py:attribute} asset_id
:canonical: algokit_subscriber.types.subscription.TransactionFilter.asset_id
:type: typing_extensions.NotRequired[int | list[int]]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.TransactionFilter.asset_id
```

````

````{py:attribute} asset_create
:canonical: algokit_subscriber.types.subscription.TransactionFilter.asset_create
:type: typing_extensions.NotRequired[bool]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.TransactionFilter.asset_create
```

````

````{py:attribute} min_amount
:canonical: algokit_subscriber.types.subscription.TransactionFilter.min_amount
:type: typing_extensions.NotRequired[int]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.TransactionFilter.min_amount
```

````

````{py:attribute} max_amount
:canonical: algokit_subscriber.types.subscription.TransactionFilter.max_amount
:type: typing_extensions.NotRequired[int]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.TransactionFilter.max_amount
```

````

````{py:attribute} method_signature
:canonical: algokit_subscriber.types.subscription.TransactionFilter.method_signature
:type: typing_extensions.NotRequired[str | list[str]]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.TransactionFilter.method_signature
```

````

````{py:attribute} app_call_arguments_match
:canonical: algokit_subscriber.types.subscription.TransactionFilter.app_call_arguments_match
:type: typing_extensions.NotRequired[collections.abc.Callable[[list[bytes] | None], bool]]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.TransactionFilter.app_call_arguments_match
```

````

````{py:attribute} arc28_events
:canonical: algokit_subscriber.types.subscription.TransactionFilter.arc28_events
:type: typing_extensions.NotRequired[list[dict[str, str]]]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.TransactionFilter.arc28_events
```

````

````{py:attribute} balance_changes
:canonical: algokit_subscriber.types.subscription.TransactionFilter.balance_changes
:type: typing_extensions.NotRequired[list[dict[str, typing.Union[int, list[int], str, list[str], algokit_subscriber.types.subscription.BalanceChangeRole, list[algokit_subscriber.types.subscription.BalanceChangeRole]]]]]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.TransactionFilter.balance_changes
```

````

````{py:attribute} custom_filter
:canonical: algokit_subscriber.types.subscription.TransactionFilter.custom_filter
:type: typing_extensions.NotRequired[collections.abc.Callable[[algokit_subscriber.types.indexer.TransactionResult], bool]]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.TransactionFilter.custom_filter
```

````

````{py:method} __contains__()
:canonical: algokit_subscriber.types.subscription.TransactionFilter.__contains__

````

````{py:method} __delattr__()
:canonical: algokit_subscriber.types.subscription.TransactionFilter.__delattr__

````

````{py:method} __delitem__()
:canonical: algokit_subscriber.types.subscription.TransactionFilter.__delitem__

````

````{py:method} __dir__()
:canonical: algokit_subscriber.types.subscription.TransactionFilter.__dir__

````

````{py:method} __eq__()
:canonical: algokit_subscriber.types.subscription.TransactionFilter.__eq__

````

````{py:method} __format__()
:canonical: algokit_subscriber.types.subscription.TransactionFilter.__format__

````

````{py:method} __ge__()
:canonical: algokit_subscriber.types.subscription.TransactionFilter.__ge__

````

````{py:method} __getattribute__()
:canonical: algokit_subscriber.types.subscription.TransactionFilter.__getattribute__

````

````{py:method} __getitem__()
:canonical: algokit_subscriber.types.subscription.TransactionFilter.__getitem__

````

````{py:method} __getstate__()
:canonical: algokit_subscriber.types.subscription.TransactionFilter.__getstate__

````

````{py:method} __gt__()
:canonical: algokit_subscriber.types.subscription.TransactionFilter.__gt__

````

````{py:method} __ior__()
:canonical: algokit_subscriber.types.subscription.TransactionFilter.__ior__

````

````{py:method} __iter__()
:canonical: algokit_subscriber.types.subscription.TransactionFilter.__iter__

````

````{py:method} __le__()
:canonical: algokit_subscriber.types.subscription.TransactionFilter.__le__

````

````{py:method} __len__()
:canonical: algokit_subscriber.types.subscription.TransactionFilter.__len__

````

````{py:method} __lt__()
:canonical: algokit_subscriber.types.subscription.TransactionFilter.__lt__

````

````{py:method} __ne__()
:canonical: algokit_subscriber.types.subscription.TransactionFilter.__ne__

````

````{py:method} __new__()
:canonical: algokit_subscriber.types.subscription.TransactionFilter.__new__

````

````{py:method} __or__()
:canonical: algokit_subscriber.types.subscription.TransactionFilter.__or__

````

````{py:method} __reduce__()
:canonical: algokit_subscriber.types.subscription.TransactionFilter.__reduce__

````

````{py:method} __reduce_ex__()
:canonical: algokit_subscriber.types.subscription.TransactionFilter.__reduce_ex__

````

````{py:method} __repr__()
:canonical: algokit_subscriber.types.subscription.TransactionFilter.__repr__

````

````{py:method} __reversed__()
:canonical: algokit_subscriber.types.subscription.TransactionFilter.__reversed__

````

````{py:method} __ror__()
:canonical: algokit_subscriber.types.subscription.TransactionFilter.__ror__

````

````{py:method} __setattr__()
:canonical: algokit_subscriber.types.subscription.TransactionFilter.__setattr__

````

````{py:method} __setitem__()
:canonical: algokit_subscriber.types.subscription.TransactionFilter.__setitem__

````

````{py:method} __sizeof__()
:canonical: algokit_subscriber.types.subscription.TransactionFilter.__sizeof__

````

````{py:method} __str__()
:canonical: algokit_subscriber.types.subscription.TransactionFilter.__str__

````

````{py:method} __subclasshook__()
:canonical: algokit_subscriber.types.subscription.TransactionFilter.__subclasshook__

````

````{py:method} clear()
:canonical: algokit_subscriber.types.subscription.TransactionFilter.clear

````

````{py:method} copy()
:canonical: algokit_subscriber.types.subscription.TransactionFilter.copy

````

````{py:method} get()
:canonical: algokit_subscriber.types.subscription.TransactionFilter.get

````

````{py:method} items()
:canonical: algokit_subscriber.types.subscription.TransactionFilter.items

````

````{py:method} keys()
:canonical: algokit_subscriber.types.subscription.TransactionFilter.keys

````

````{py:method} pop()
:canonical: algokit_subscriber.types.subscription.TransactionFilter.pop

````

````{py:method} popitem()
:canonical: algokit_subscriber.types.subscription.TransactionFilter.popitem

````

````{py:method} setdefault()
:canonical: algokit_subscriber.types.subscription.TransactionFilter.setdefault

````

````{py:method} update()
:canonical: algokit_subscriber.types.subscription.TransactionFilter.update

````

````{py:method} values()
:canonical: algokit_subscriber.types.subscription.TransactionFilter.values

````

`````

`````{py:class} NamedTransactionFilter()
:canonical: algokit_subscriber.types.subscription.NamedTransactionFilter

Bases: {py:obj}`typing.TypedDict`

```{autodoc2-docstring} algokit_subscriber.types.subscription.NamedTransactionFilter
```

```{rubric} Initialization
```

```{autodoc2-docstring} algokit_subscriber.types.subscription.NamedTransactionFilter.__init__
```

````{py:attribute} name
:canonical: algokit_subscriber.types.subscription.NamedTransactionFilter.name
:type: str
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.NamedTransactionFilter.name
```

````

````{py:attribute} filter
:canonical: algokit_subscriber.types.subscription.NamedTransactionFilter.filter
:type: algokit_subscriber.types.subscription.TransactionFilter
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.NamedTransactionFilter.filter
```

````

````{py:method} __contains__()
:canonical: algokit_subscriber.types.subscription.NamedTransactionFilter.__contains__

````

````{py:method} __delattr__()
:canonical: algokit_subscriber.types.subscription.NamedTransactionFilter.__delattr__

````

````{py:method} __delitem__()
:canonical: algokit_subscriber.types.subscription.NamedTransactionFilter.__delitem__

````

````{py:method} __dir__()
:canonical: algokit_subscriber.types.subscription.NamedTransactionFilter.__dir__

````

````{py:method} __eq__()
:canonical: algokit_subscriber.types.subscription.NamedTransactionFilter.__eq__

````

````{py:method} __format__()
:canonical: algokit_subscriber.types.subscription.NamedTransactionFilter.__format__

````

````{py:method} __ge__()
:canonical: algokit_subscriber.types.subscription.NamedTransactionFilter.__ge__

````

````{py:method} __getattribute__()
:canonical: algokit_subscriber.types.subscription.NamedTransactionFilter.__getattribute__

````

````{py:method} __getitem__()
:canonical: algokit_subscriber.types.subscription.NamedTransactionFilter.__getitem__

````

````{py:method} __getstate__()
:canonical: algokit_subscriber.types.subscription.NamedTransactionFilter.__getstate__

````

````{py:method} __gt__()
:canonical: algokit_subscriber.types.subscription.NamedTransactionFilter.__gt__

````

````{py:method} __ior__()
:canonical: algokit_subscriber.types.subscription.NamedTransactionFilter.__ior__

````

````{py:method} __iter__()
:canonical: algokit_subscriber.types.subscription.NamedTransactionFilter.__iter__

````

````{py:method} __le__()
:canonical: algokit_subscriber.types.subscription.NamedTransactionFilter.__le__

````

````{py:method} __len__()
:canonical: algokit_subscriber.types.subscription.NamedTransactionFilter.__len__

````

````{py:method} __lt__()
:canonical: algokit_subscriber.types.subscription.NamedTransactionFilter.__lt__

````

````{py:method} __ne__()
:canonical: algokit_subscriber.types.subscription.NamedTransactionFilter.__ne__

````

````{py:method} __new__()
:canonical: algokit_subscriber.types.subscription.NamedTransactionFilter.__new__

````

````{py:method} __or__()
:canonical: algokit_subscriber.types.subscription.NamedTransactionFilter.__or__

````

````{py:method} __reduce__()
:canonical: algokit_subscriber.types.subscription.NamedTransactionFilter.__reduce__

````

````{py:method} __reduce_ex__()
:canonical: algokit_subscriber.types.subscription.NamedTransactionFilter.__reduce_ex__

````

````{py:method} __repr__()
:canonical: algokit_subscriber.types.subscription.NamedTransactionFilter.__repr__

````

````{py:method} __reversed__()
:canonical: algokit_subscriber.types.subscription.NamedTransactionFilter.__reversed__

````

````{py:method} __ror__()
:canonical: algokit_subscriber.types.subscription.NamedTransactionFilter.__ror__

````

````{py:method} __setattr__()
:canonical: algokit_subscriber.types.subscription.NamedTransactionFilter.__setattr__

````

````{py:method} __setitem__()
:canonical: algokit_subscriber.types.subscription.NamedTransactionFilter.__setitem__

````

````{py:method} __sizeof__()
:canonical: algokit_subscriber.types.subscription.NamedTransactionFilter.__sizeof__

````

````{py:method} __str__()
:canonical: algokit_subscriber.types.subscription.NamedTransactionFilter.__str__

````

````{py:method} __subclasshook__()
:canonical: algokit_subscriber.types.subscription.NamedTransactionFilter.__subclasshook__

````

````{py:method} clear()
:canonical: algokit_subscriber.types.subscription.NamedTransactionFilter.clear

````

````{py:method} copy()
:canonical: algokit_subscriber.types.subscription.NamedTransactionFilter.copy

````

````{py:method} get()
:canonical: algokit_subscriber.types.subscription.NamedTransactionFilter.get

````

````{py:method} items()
:canonical: algokit_subscriber.types.subscription.NamedTransactionFilter.items

````

````{py:method} keys()
:canonical: algokit_subscriber.types.subscription.NamedTransactionFilter.keys

````

````{py:method} pop()
:canonical: algokit_subscriber.types.subscription.NamedTransactionFilter.pop

````

````{py:method} popitem()
:canonical: algokit_subscriber.types.subscription.NamedTransactionFilter.popitem

````

````{py:method} setdefault()
:canonical: algokit_subscriber.types.subscription.NamedTransactionFilter.setdefault

````

````{py:method} update()
:canonical: algokit_subscriber.types.subscription.NamedTransactionFilter.update

````

````{py:method} values()
:canonical: algokit_subscriber.types.subscription.NamedTransactionFilter.values

````

`````

`````{py:class} CoreTransactionSubscriptionParams()
:canonical: algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams

Bases: {py:obj}`typing.TypedDict`

````{py:attribute} filters
:canonical: algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.filters
:type: list[algokit_subscriber.types.subscription.NamedTransactionFilter]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.filters
```

````

````{py:attribute} arc28_events
:canonical: algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.arc28_events
:type: typing_extensions.NotRequired[list[algokit_subscriber.types.arc28.Arc28EventGroup]]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.arc28_events
```

````

````{py:attribute} max_rounds_to_sync
:canonical: algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.max_rounds_to_sync
:type: typing_extensions.NotRequired[int | None]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.max_rounds_to_sync
```

````

````{py:attribute} max_indexer_rounds_to_sync
:canonical: algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.max_indexer_rounds_to_sync
:type: typing_extensions.NotRequired[int | None]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.max_indexer_rounds_to_sync
```

````

````{py:attribute} sync_behaviour
:canonical: algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.sync_behaviour
:type: typing.Literal[catchup-with-algod, catchup-with-indexer, fail, skip-sync-newest, sync-oldest, sync-oldest-start-now]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.sync_behaviour
```

````

````{py:method} __contains__()
:canonical: algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.__contains__

````

````{py:method} __delattr__()
:canonical: algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.__delattr__

````

````{py:method} __delitem__()
:canonical: algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.__delitem__

````

````{py:method} __dir__()
:canonical: algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.__dir__

````

````{py:method} __eq__()
:canonical: algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.__eq__

````

````{py:method} __format__()
:canonical: algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.__format__

````

````{py:method} __ge__()
:canonical: algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.__ge__

````

````{py:method} __getattribute__()
:canonical: algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.__getattribute__

````

````{py:method} __getitem__()
:canonical: algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.__getitem__

````

````{py:method} __getstate__()
:canonical: algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.__getstate__

````

````{py:method} __gt__()
:canonical: algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.__gt__

````

````{py:method} __ior__()
:canonical: algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.__ior__

````

````{py:method} __iter__()
:canonical: algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.__iter__

````

````{py:method} __le__()
:canonical: algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.__le__

````

````{py:method} __len__()
:canonical: algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.__len__

````

````{py:method} __lt__()
:canonical: algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.__lt__

````

````{py:method} __ne__()
:canonical: algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.__ne__

````

````{py:method} __new__()
:canonical: algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.__new__

````

````{py:method} __or__()
:canonical: algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.__or__

````

````{py:method} __reduce__()
:canonical: algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.__reduce__

````

````{py:method} __reduce_ex__()
:canonical: algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.__reduce_ex__

````

````{py:method} __repr__()
:canonical: algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.__repr__

````

````{py:method} __reversed__()
:canonical: algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.__reversed__

````

````{py:method} __ror__()
:canonical: algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.__ror__

````

````{py:method} __setattr__()
:canonical: algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.__setattr__

````

````{py:method} __setitem__()
:canonical: algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.__setitem__

````

````{py:method} __sizeof__()
:canonical: algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.__sizeof__

````

````{py:method} __str__()
:canonical: algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.__str__

````

````{py:method} __subclasshook__()
:canonical: algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.__subclasshook__

````

````{py:method} clear()
:canonical: algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.clear

````

````{py:method} copy()
:canonical: algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.copy

````

````{py:method} get()
:canonical: algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.get

````

````{py:method} items()
:canonical: algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.items

````

````{py:method} keys()
:canonical: algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.keys

````

````{py:method} pop()
:canonical: algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.pop

````

````{py:method} popitem()
:canonical: algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.popitem

````

````{py:method} setdefault()
:canonical: algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.setdefault

````

````{py:method} update()
:canonical: algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.update

````

````{py:method} values()
:canonical: algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams.values

````

`````

`````{py:class} TransactionSubscriptionParams()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionParams

Bases: {py:obj}`algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams`

````{py:attribute} watermark
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionParams.watermark
:type: int
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.TransactionSubscriptionParams.watermark
```

````

````{py:attribute} current_round
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionParams.current_round
:type: typing_extensions.NotRequired[int]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.TransactionSubscriptionParams.current_round
```

````

````{py:attribute} filters
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionParams.filters
:type: list[algokit_subscriber.types.subscription.NamedTransactionFilter]
:value: >
   None

````

````{py:attribute} arc28_events
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionParams.arc28_events
:type: typing_extensions.NotRequired[list[algokit_subscriber.types.arc28.Arc28EventGroup]]
:value: >
   None

````

````{py:attribute} max_rounds_to_sync
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionParams.max_rounds_to_sync
:type: typing_extensions.NotRequired[int | None]
:value: >
   None

````

````{py:attribute} max_indexer_rounds_to_sync
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionParams.max_indexer_rounds_to_sync
:type: typing_extensions.NotRequired[int | None]
:value: >
   None

````

````{py:attribute} sync_behaviour
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionParams.sync_behaviour
:type: typing.Literal[catchup-with-algod, catchup-with-indexer, fail, skip-sync-newest, sync-oldest, sync-oldest-start-now]
:value: >
   None

````

````{py:method} __contains__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionParams.__contains__

````

````{py:method} __delattr__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionParams.__delattr__

````

````{py:method} __delitem__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionParams.__delitem__

````

````{py:method} __dir__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionParams.__dir__

````

````{py:method} __eq__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionParams.__eq__

````

````{py:method} __format__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionParams.__format__

````

````{py:method} __ge__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionParams.__ge__

````

````{py:method} __getattribute__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionParams.__getattribute__

````

````{py:method} __getitem__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionParams.__getitem__

````

````{py:method} __getstate__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionParams.__getstate__

````

````{py:method} __gt__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionParams.__gt__

````

````{py:method} __ior__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionParams.__ior__

````

````{py:method} __iter__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionParams.__iter__

````

````{py:method} __le__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionParams.__le__

````

````{py:method} __len__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionParams.__len__

````

````{py:method} __lt__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionParams.__lt__

````

````{py:method} __ne__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionParams.__ne__

````

````{py:method} __new__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionParams.__new__

````

````{py:method} __or__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionParams.__or__

````

````{py:method} __reduce__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionParams.__reduce__

````

````{py:method} __reduce_ex__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionParams.__reduce_ex__

````

````{py:method} __repr__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionParams.__repr__

````

````{py:method} __reversed__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionParams.__reversed__

````

````{py:method} __ror__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionParams.__ror__

````

````{py:method} __setattr__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionParams.__setattr__

````

````{py:method} __setitem__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionParams.__setitem__

````

````{py:method} __sizeof__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionParams.__sizeof__

````

````{py:method} __str__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionParams.__str__

````

````{py:method} __subclasshook__()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionParams.__subclasshook__

````

````{py:method} clear()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionParams.clear

````

````{py:method} copy()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionParams.copy

````

````{py:method} get()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionParams.get

````

````{py:method} items()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionParams.items

````

````{py:method} keys()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionParams.keys

````

````{py:method} pop()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionParams.pop

````

````{py:method} popitem()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionParams.popitem

````

````{py:method} setdefault()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionParams.setdefault

````

````{py:method} update()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionParams.update

````

````{py:method} values()
:canonical: algokit_subscriber.types.subscription.TransactionSubscriptionParams.values

````

`````

`````{py:class} WatermarkPersistence()
:canonical: algokit_subscriber.types.subscription.WatermarkPersistence

Bases: {py:obj}`typing.TypedDict`

````{py:attribute} get
:canonical: algokit_subscriber.types.subscription.WatermarkPersistence.get
:type: collections.abc.Callable[[], int | None]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.WatermarkPersistence.get
```

````

````{py:attribute} set
:canonical: algokit_subscriber.types.subscription.WatermarkPersistence.set
:type: collections.abc.Callable[[int], None]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.WatermarkPersistence.set
```

````

````{py:method} __contains__()
:canonical: algokit_subscriber.types.subscription.WatermarkPersistence.__contains__

````

````{py:method} __delattr__()
:canonical: algokit_subscriber.types.subscription.WatermarkPersistence.__delattr__

````

````{py:method} __delitem__()
:canonical: algokit_subscriber.types.subscription.WatermarkPersistence.__delitem__

````

````{py:method} __dir__()
:canonical: algokit_subscriber.types.subscription.WatermarkPersistence.__dir__

````

````{py:method} __eq__()
:canonical: algokit_subscriber.types.subscription.WatermarkPersistence.__eq__

````

````{py:method} __format__()
:canonical: algokit_subscriber.types.subscription.WatermarkPersistence.__format__

````

````{py:method} __ge__()
:canonical: algokit_subscriber.types.subscription.WatermarkPersistence.__ge__

````

````{py:method} __getattribute__()
:canonical: algokit_subscriber.types.subscription.WatermarkPersistence.__getattribute__

````

````{py:method} __getitem__()
:canonical: algokit_subscriber.types.subscription.WatermarkPersistence.__getitem__

````

````{py:method} __getstate__()
:canonical: algokit_subscriber.types.subscription.WatermarkPersistence.__getstate__

````

````{py:method} __gt__()
:canonical: algokit_subscriber.types.subscription.WatermarkPersistence.__gt__

````

````{py:method} __ior__()
:canonical: algokit_subscriber.types.subscription.WatermarkPersistence.__ior__

````

````{py:method} __iter__()
:canonical: algokit_subscriber.types.subscription.WatermarkPersistence.__iter__

````

````{py:method} __le__()
:canonical: algokit_subscriber.types.subscription.WatermarkPersistence.__le__

````

````{py:method} __len__()
:canonical: algokit_subscriber.types.subscription.WatermarkPersistence.__len__

````

````{py:method} __lt__()
:canonical: algokit_subscriber.types.subscription.WatermarkPersistence.__lt__

````

````{py:method} __ne__()
:canonical: algokit_subscriber.types.subscription.WatermarkPersistence.__ne__

````

````{py:method} __new__()
:canonical: algokit_subscriber.types.subscription.WatermarkPersistence.__new__

````

````{py:method} __or__()
:canonical: algokit_subscriber.types.subscription.WatermarkPersistence.__or__

````

````{py:method} __reduce__()
:canonical: algokit_subscriber.types.subscription.WatermarkPersistence.__reduce__

````

````{py:method} __reduce_ex__()
:canonical: algokit_subscriber.types.subscription.WatermarkPersistence.__reduce_ex__

````

````{py:method} __repr__()
:canonical: algokit_subscriber.types.subscription.WatermarkPersistence.__repr__

````

````{py:method} __reversed__()
:canonical: algokit_subscriber.types.subscription.WatermarkPersistence.__reversed__

````

````{py:method} __ror__()
:canonical: algokit_subscriber.types.subscription.WatermarkPersistence.__ror__

````

````{py:method} __setattr__()
:canonical: algokit_subscriber.types.subscription.WatermarkPersistence.__setattr__

````

````{py:method} __setitem__()
:canonical: algokit_subscriber.types.subscription.WatermarkPersistence.__setitem__

````

````{py:method} __sizeof__()
:canonical: algokit_subscriber.types.subscription.WatermarkPersistence.__sizeof__

````

````{py:method} __str__()
:canonical: algokit_subscriber.types.subscription.WatermarkPersistence.__str__

````

````{py:method} __subclasshook__()
:canonical: algokit_subscriber.types.subscription.WatermarkPersistence.__subclasshook__

````

````{py:method} clear()
:canonical: algokit_subscriber.types.subscription.WatermarkPersistence.clear

````

````{py:method} copy()
:canonical: algokit_subscriber.types.subscription.WatermarkPersistence.copy

````

````{py:method} items()
:canonical: algokit_subscriber.types.subscription.WatermarkPersistence.items

````

````{py:method} keys()
:canonical: algokit_subscriber.types.subscription.WatermarkPersistence.keys

````

````{py:method} pop()
:canonical: algokit_subscriber.types.subscription.WatermarkPersistence.pop

````

````{py:method} popitem()
:canonical: algokit_subscriber.types.subscription.WatermarkPersistence.popitem

````

````{py:method} setdefault()
:canonical: algokit_subscriber.types.subscription.WatermarkPersistence.setdefault

````

````{py:method} update()
:canonical: algokit_subscriber.types.subscription.WatermarkPersistence.update

````

````{py:method} values()
:canonical: algokit_subscriber.types.subscription.WatermarkPersistence.values

````

`````

`````{py:class} AlgorandSubscriberConfig()
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig

Bases: {py:obj}`algokit_subscriber.types.subscription.CoreTransactionSubscriptionParams`

```{autodoc2-docstring} algokit_subscriber.types.subscription.AlgorandSubscriberConfig
```

```{rubric} Initialization
```

```{autodoc2-docstring} algokit_subscriber.types.subscription.AlgorandSubscriberConfig.__init__
```

````{py:attribute} filters
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig.filters
:type: list[SubscriberConfigFilter]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.AlgorandSubscriberConfig.filters
```

````

````{py:attribute} frequency_in_seconds
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig.frequency_in_seconds
:type: typing_extensions.NotRequired[int]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.AlgorandSubscriberConfig.frequency_in_seconds
```

````

````{py:attribute} wait_for_block_when_at_tip
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig.wait_for_block_when_at_tip
:type: typing_extensions.NotRequired[bool]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.AlgorandSubscriberConfig.wait_for_block_when_at_tip
```

````

````{py:attribute} watermark_persistence
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig.watermark_persistence
:type: algokit_subscriber.types.subscription.WatermarkPersistence
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.AlgorandSubscriberConfig.watermark_persistence
```

````

````{py:attribute} arc28_events
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig.arc28_events
:type: typing_extensions.NotRequired[list[algokit_subscriber.types.arc28.Arc28EventGroup]]
:value: >
   None

````

````{py:attribute} max_rounds_to_sync
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig.max_rounds_to_sync
:type: typing_extensions.NotRequired[int | None]
:value: >
   None

````

````{py:attribute} max_indexer_rounds_to_sync
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig.max_indexer_rounds_to_sync
:type: typing_extensions.NotRequired[int | None]
:value: >
   None

````

````{py:attribute} sync_behaviour
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig.sync_behaviour
:type: typing.Literal[catchup-with-algod, catchup-with-indexer, fail, skip-sync-newest, sync-oldest, sync-oldest-start-now]
:value: >
   None

````

````{py:method} __contains__()
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig.__contains__

````

````{py:method} __delattr__()
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig.__delattr__

````

````{py:method} __delitem__()
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig.__delitem__

````

````{py:method} __dir__()
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig.__dir__

````

````{py:method} __eq__()
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig.__eq__

````

````{py:method} __format__()
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig.__format__

````

````{py:method} __ge__()
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig.__ge__

````

````{py:method} __getattribute__()
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig.__getattribute__

````

````{py:method} __getitem__()
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig.__getitem__

````

````{py:method} __getstate__()
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig.__getstate__

````

````{py:method} __gt__()
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig.__gt__

````

````{py:method} __ior__()
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig.__ior__

````

````{py:method} __iter__()
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig.__iter__

````

````{py:method} __le__()
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig.__le__

````

````{py:method} __len__()
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig.__len__

````

````{py:method} __lt__()
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig.__lt__

````

````{py:method} __ne__()
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig.__ne__

````

````{py:method} __new__()
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig.__new__

````

````{py:method} __or__()
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig.__or__

````

````{py:method} __reduce__()
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig.__reduce__

````

````{py:method} __reduce_ex__()
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig.__reduce_ex__

````

````{py:method} __repr__()
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig.__repr__

````

````{py:method} __reversed__()
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig.__reversed__

````

````{py:method} __ror__()
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig.__ror__

````

````{py:method} __setattr__()
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig.__setattr__

````

````{py:method} __setitem__()
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig.__setitem__

````

````{py:method} __sizeof__()
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig.__sizeof__

````

````{py:method} __str__()
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig.__str__

````

````{py:method} __subclasshook__()
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig.__subclasshook__

````

````{py:method} clear()
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig.clear

````

````{py:method} copy()
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig.copy

````

````{py:method} get()
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig.get

````

````{py:method} items()
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig.items

````

````{py:method} keys()
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig.keys

````

````{py:method} pop()
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig.pop

````

````{py:method} popitem()
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig.popitem

````

````{py:method} setdefault()
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig.setdefault

````

````{py:method} update()
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig.update

````

````{py:method} values()
:canonical: algokit_subscriber.types.subscription.AlgorandSubscriberConfig.values

````

`````

`````{py:class} SubscriberConfigFilter()
:canonical: algokit_subscriber.types.subscription.SubscriberConfigFilter

Bases: {py:obj}`algokit_subscriber.types.subscription.NamedTransactionFilter`

```{autodoc2-docstring} algokit_subscriber.types.subscription.SubscriberConfigFilter
```

```{rubric} Initialization
```

```{autodoc2-docstring} algokit_subscriber.types.subscription.SubscriberConfigFilter.__init__
```

````{py:attribute} mapper
:canonical: algokit_subscriber.types.subscription.SubscriberConfigFilter.mapper
:type: typing_extensions.NotRequired[collections.abc.Callable[[list[algokit_subscriber.types.subscription.SubscribedTransaction]], list[typing.Any]]]
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.subscription.SubscriberConfigFilter.mapper
```

````

````{py:attribute} name
:canonical: algokit_subscriber.types.subscription.SubscriberConfigFilter.name
:type: str
:value: >
   None

````

````{py:attribute} filter
:canonical: algokit_subscriber.types.subscription.SubscriberConfigFilter.filter
:type: algokit_subscriber.types.subscription.TransactionFilter
:value: >
   None

````

````{py:method} __contains__()
:canonical: algokit_subscriber.types.subscription.SubscriberConfigFilter.__contains__

````

````{py:method} __delattr__()
:canonical: algokit_subscriber.types.subscription.SubscriberConfigFilter.__delattr__

````

````{py:method} __delitem__()
:canonical: algokit_subscriber.types.subscription.SubscriberConfigFilter.__delitem__

````

````{py:method} __dir__()
:canonical: algokit_subscriber.types.subscription.SubscriberConfigFilter.__dir__

````

````{py:method} __eq__()
:canonical: algokit_subscriber.types.subscription.SubscriberConfigFilter.__eq__

````

````{py:method} __format__()
:canonical: algokit_subscriber.types.subscription.SubscriberConfigFilter.__format__

````

````{py:method} __ge__()
:canonical: algokit_subscriber.types.subscription.SubscriberConfigFilter.__ge__

````

````{py:method} __getattribute__()
:canonical: algokit_subscriber.types.subscription.SubscriberConfigFilter.__getattribute__

````

````{py:method} __getitem__()
:canonical: algokit_subscriber.types.subscription.SubscriberConfigFilter.__getitem__

````

````{py:method} __getstate__()
:canonical: algokit_subscriber.types.subscription.SubscriberConfigFilter.__getstate__

````

````{py:method} __gt__()
:canonical: algokit_subscriber.types.subscription.SubscriberConfigFilter.__gt__

````

````{py:method} __ior__()
:canonical: algokit_subscriber.types.subscription.SubscriberConfigFilter.__ior__

````

````{py:method} __iter__()
:canonical: algokit_subscriber.types.subscription.SubscriberConfigFilter.__iter__

````

````{py:method} __le__()
:canonical: algokit_subscriber.types.subscription.SubscriberConfigFilter.__le__

````

````{py:method} __len__()
:canonical: algokit_subscriber.types.subscription.SubscriberConfigFilter.__len__

````

````{py:method} __lt__()
:canonical: algokit_subscriber.types.subscription.SubscriberConfigFilter.__lt__

````

````{py:method} __ne__()
:canonical: algokit_subscriber.types.subscription.SubscriberConfigFilter.__ne__

````

````{py:method} __new__()
:canonical: algokit_subscriber.types.subscription.SubscriberConfigFilter.__new__

````

````{py:method} __or__()
:canonical: algokit_subscriber.types.subscription.SubscriberConfigFilter.__or__

````

````{py:method} __reduce__()
:canonical: algokit_subscriber.types.subscription.SubscriberConfigFilter.__reduce__

````

````{py:method} __reduce_ex__()
:canonical: algokit_subscriber.types.subscription.SubscriberConfigFilter.__reduce_ex__

````

````{py:method} __repr__()
:canonical: algokit_subscriber.types.subscription.SubscriberConfigFilter.__repr__

````

````{py:method} __reversed__()
:canonical: algokit_subscriber.types.subscription.SubscriberConfigFilter.__reversed__

````

````{py:method} __ror__()
:canonical: algokit_subscriber.types.subscription.SubscriberConfigFilter.__ror__

````

````{py:method} __setattr__()
:canonical: algokit_subscriber.types.subscription.SubscriberConfigFilter.__setattr__

````

````{py:method} __setitem__()
:canonical: algokit_subscriber.types.subscription.SubscriberConfigFilter.__setitem__

````

````{py:method} __sizeof__()
:canonical: algokit_subscriber.types.subscription.SubscriberConfigFilter.__sizeof__

````

````{py:method} __str__()
:canonical: algokit_subscriber.types.subscription.SubscriberConfigFilter.__str__

````

````{py:method} __subclasshook__()
:canonical: algokit_subscriber.types.subscription.SubscriberConfigFilter.__subclasshook__

````

````{py:method} clear()
:canonical: algokit_subscriber.types.subscription.SubscriberConfigFilter.clear

````

````{py:method} copy()
:canonical: algokit_subscriber.types.subscription.SubscriberConfigFilter.copy

````

````{py:method} get()
:canonical: algokit_subscriber.types.subscription.SubscriberConfigFilter.get

````

````{py:method} items()
:canonical: algokit_subscriber.types.subscription.SubscriberConfigFilter.items

````

````{py:method} keys()
:canonical: algokit_subscriber.types.subscription.SubscriberConfigFilter.keys

````

````{py:method} pop()
:canonical: algokit_subscriber.types.subscription.SubscriberConfigFilter.pop

````

````{py:method} popitem()
:canonical: algokit_subscriber.types.subscription.SubscriberConfigFilter.popitem

````

````{py:method} setdefault()
:canonical: algokit_subscriber.types.subscription.SubscriberConfigFilter.setdefault

````

````{py:method} update()
:canonical: algokit_subscriber.types.subscription.SubscriberConfigFilter.update

````

````{py:method} values()
:canonical: algokit_subscriber.types.subscription.SubscriberConfigFilter.values

````

`````
