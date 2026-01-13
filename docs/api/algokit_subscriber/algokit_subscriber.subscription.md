# {py:mod}`algokit_subscriber.subscription`

```{py:module} algokit_subscriber.subscription
```

```{autodoc2-docstring} algokit_subscriber.subscription
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`deduplicate_subscribed_transactions <algokit_subscriber.subscription.deduplicate_subscribed_transactions>`
  - ```{autodoc2-docstring} algokit_subscriber.subscription.deduplicate_subscribed_transactions
    :summary:
    ```
* - {py:obj}`transaction_is_in_arc28_event_group <algokit_subscriber.subscription.transaction_is_in_arc28_event_group>`
  - ```{autodoc2-docstring} algokit_subscriber.subscription.transaction_is_in_arc28_event_group
    :summary:
    ```
* - {py:obj}`has_emitted_matching_arc28_event <algokit_subscriber.subscription.has_emitted_matching_arc28_event>`
  - ```{autodoc2-docstring} algokit_subscriber.subscription.has_emitted_matching_arc28_event
    :summary:
    ```
* - {py:obj}`extract_arc28_events <algokit_subscriber.subscription.extract_arc28_events>`
  - ```{autodoc2-docstring} algokit_subscriber.subscription.extract_arc28_events
    :summary:
    ```
* - {py:obj}`indexer_pre_filter <algokit_subscriber.subscription.indexer_pre_filter>`
  - ```{autodoc2-docstring} algokit_subscriber.subscription.indexer_pre_filter
    :summary:
    ```
* - {py:obj}`indexer_pre_filter_in_memory <algokit_subscriber.subscription.indexer_pre_filter_in_memory>`
  - ```{autodoc2-docstring} algokit_subscriber.subscription.indexer_pre_filter_in_memory
    :summary:
    ```
* - {py:obj}`get_method_selector_base64 <algokit_subscriber.subscription.get_method_selector_base64>`
  - ```{autodoc2-docstring} algokit_subscriber.subscription.get_method_selector_base64
    :summary:
    ```
* - {py:obj}`has_balance_change_match <algokit_subscriber.subscription.has_balance_change_match>`
  - ```{autodoc2-docstring} algokit_subscriber.subscription.has_balance_change_match
    :summary:
    ```
* - {py:obj}`get_subscribed_transactions <algokit_subscriber.subscription.get_subscribed_transactions>`
  - ```{autodoc2-docstring} algokit_subscriber.subscription.get_subscribed_transactions
    :summary:
    ```
* - {py:obj}`process_extra_fields <algokit_subscriber.subscription.process_extra_fields>`
  - ```{autodoc2-docstring} algokit_subscriber.subscription.process_extra_fields
    :summary:
    ```
* - {py:obj}`extract_balance_changes_from_indexer_transaction <algokit_subscriber.subscription.extract_balance_changes_from_indexer_transaction>`
  - ```{autodoc2-docstring} algokit_subscriber.subscription.extract_balance_changes_from_indexer_transaction
    :summary:
    ```
* - {py:obj}`get_filtered_indexer_transactions <algokit_subscriber.subscription.get_filtered_indexer_transactions>`
  - ```{autodoc2-docstring} algokit_subscriber.subscription.get_filtered_indexer_transactions
    :summary:
    ```
* - {py:obj}`get_indexer_inner_transactions <algokit_subscriber.subscription.get_indexer_inner_transactions>`
  - ```{autodoc2-docstring} algokit_subscriber.subscription.get_indexer_inner_transactions
    :summary:
    ```
* - {py:obj}`indexer_post_filter <algokit_subscriber.subscription.indexer_post_filter>`
  - ```{autodoc2-docstring} algokit_subscriber.subscription.indexer_post_filter
    :summary:
    ```
* - {py:obj}`transaction_filter <algokit_subscriber.subscription.transaction_filter>`
  - ```{autodoc2-docstring} algokit_subscriber.subscription.transaction_filter
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`SearchForTransactions <algokit_subscriber.subscription.SearchForTransactions>`
  - ```{autodoc2-docstring} algokit_subscriber.subscription.SearchForTransactions
    :summary:
    ```
````

### API

````{py:data} SearchForTransactions
:canonical: algokit_subscriber.subscription.SearchForTransactions
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.subscription.SearchForTransactions
```

````

````{py:function} deduplicate_subscribed_transactions(txns: list[algokit_subscriber.types.subscription.SubscribedTransaction]) -> list[algokit_subscriber.types.subscription.SubscribedTransaction]
:canonical: algokit_subscriber.subscription.deduplicate_subscribed_transactions

```{autodoc2-docstring} algokit_subscriber.subscription.deduplicate_subscribed_transactions
```
````

````{py:function} transaction_is_in_arc28_event_group(group: algokit_subscriber.types.arc28.Arc28EventGroup, app_id: int, transaction: collections.abc.Callable[[], algokit_subscriber.types.indexer.TransactionResult]) -> bool
:canonical: algokit_subscriber.subscription.transaction_is_in_arc28_event_group

```{autodoc2-docstring} algokit_subscriber.subscription.transaction_is_in_arc28_event_group
```
````

````{py:function} has_emitted_matching_arc28_event(logs: list[str], all_events: list[algokit_subscriber.types.arc28.Arc28EventToProcess], event_groups: list[algokit_subscriber.types.arc28.Arc28EventGroup], event_filter: list[dict[str, str]], app_id: int, transaction: collections.abc.Callable[[], algokit_subscriber.types.indexer.TransactionResult]) -> bool
:canonical: algokit_subscriber.subscription.has_emitted_matching_arc28_event

```{autodoc2-docstring} algokit_subscriber.subscription.has_emitted_matching_arc28_event
```
````

````{py:function} extract_arc28_events(transaction_id: str, logs: list[bytes], events: list[algokit_subscriber.types.arc28.Arc28EventToProcess], continue_on_error: collections.abc.Callable[[str], bool]) -> list[algokit_subscriber.types.arc28.EmittedArc28Event]
:canonical: algokit_subscriber.subscription.extract_arc28_events

```{autodoc2-docstring} algokit_subscriber.subscription.extract_arc28_events
```
````

````{py:function} indexer_pre_filter(subscription: algokit_subscriber.types.subscription.TransactionFilter, min_round: int, max_round: int) -> dict[str, typing.Any]
:canonical: algokit_subscriber.subscription.indexer_pre_filter

```{autodoc2-docstring} algokit_subscriber.subscription.indexer_pre_filter
```
````

````{py:function} indexer_pre_filter_in_memory(subscription: algokit_subscriber.types.subscription.TransactionFilter) -> collections.abc.Callable[[algokit_subscriber.types.indexer.TransactionResult], bool]
:canonical: algokit_subscriber.subscription.indexer_pre_filter_in_memory

```{autodoc2-docstring} algokit_subscriber.subscription.indexer_pre_filter_in_memory
```
````

````{py:function} get_method_selector_base64(method_signature: str) -> str
:canonical: algokit_subscriber.subscription.get_method_selector_base64

```{autodoc2-docstring} algokit_subscriber.subscription.get_method_selector_base64
```
````

````{py:function} has_balance_change_match(transaction_balance_changes: list[algokit_subscriber.types.subscription.BalanceChange], filtered_balance_changes: list[dict[str, typing.Any]] | None) -> bool
:canonical: algokit_subscriber.subscription.has_balance_change_match

```{autodoc2-docstring} algokit_subscriber.subscription.has_balance_change_match
```
````

````{py:function} get_subscribed_transactions(subscription: algokit_subscriber.types.subscription.TransactionSubscriptionParams, algod: algosdk.v2client.algod.AlgodClient, indexer: algosdk.v2client.indexer.IndexerClient | None = None) -> algokit_subscriber.types.subscription.TransactionSubscriptionResult
:canonical: algokit_subscriber.subscription.get_subscribed_transactions

```{autodoc2-docstring} algokit_subscriber.subscription.get_subscribed_transactions
```
````

````{py:function} process_extra_fields(transaction: algokit_subscriber.types.indexer.TransactionResult | algokit_subscriber.types.subscription.SubscribedTransaction, arc28_events: list[algokit_subscriber.types.arc28.Arc28EventToProcess], arc28_groups: list[algokit_subscriber.types.arc28.Arc28EventGroup]) -> algokit_subscriber.types.subscription.SubscribedTransaction
:canonical: algokit_subscriber.subscription.process_extra_fields

```{autodoc2-docstring} algokit_subscriber.subscription.process_extra_fields
```
````

````{py:function} extract_balance_changes_from_indexer_transaction(transaction: algokit_subscriber.types.indexer.TransactionResult) -> list[algokit_subscriber.types.subscription.BalanceChange]
:canonical: algokit_subscriber.subscription.extract_balance_changes_from_indexer_transaction

```{autodoc2-docstring} algokit_subscriber.subscription.extract_balance_changes_from_indexer_transaction
```
````

````{py:function} get_filtered_indexer_transactions(transaction: algokit_subscriber.types.indexer.TransactionResult, txn_filter: algokit_subscriber.types.subscription.NamedTransactionFilter) -> list[algokit_subscriber.types.subscription.SubscribedTransaction]
:canonical: algokit_subscriber.subscription.get_filtered_indexer_transactions

```{autodoc2-docstring} algokit_subscriber.subscription.get_filtered_indexer_transactions
```
````

````{py:function} get_indexer_inner_transactions(root: algokit_subscriber.types.indexer.TransactionResult, parent: algokit_subscriber.types.indexer.TransactionResult, offset: collections.abc.Callable) -> list[algokit_subscriber.types.subscription.SubscribedTransaction]
:canonical: algokit_subscriber.subscription.get_indexer_inner_transactions

```{autodoc2-docstring} algokit_subscriber.subscription.get_indexer_inner_transactions
```
````

````{py:function} indexer_post_filter(subscription: algokit_subscriber.types.subscription.TransactionFilter, arc28_events: list[algokit_subscriber.types.arc28.Arc28EventToProcess], arc28_event_groups: list[algokit_subscriber.types.arc28.Arc28EventGroup]) -> collections.abc.Callable[[algokit_subscriber.types.indexer.TransactionResult], bool]
:canonical: algokit_subscriber.subscription.indexer_post_filter

```{autodoc2-docstring} algokit_subscriber.subscription.indexer_post_filter
```
````

````{py:function} transaction_filter(subscription: algokit_subscriber.types.subscription.TransactionFilter, arc28_events: list[algokit_subscriber.types.arc28.Arc28EventToProcess], arc28_event_groups: list[algokit_subscriber.types.arc28.Arc28EventGroup]) -> collections.abc.Callable[[algokit_subscriber.types.block.TransactionInBlock], bool]
:canonical: algokit_subscriber.subscription.transaction_filter

```{autodoc2-docstring} algokit_subscriber.subscription.transaction_filter
```
````
