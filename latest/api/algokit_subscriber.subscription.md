---
title: algokit_subscriber.subscription
---

# [`algokit_subscriber.subscription`](#module-algokit_subscriber.subscription)

## Module Contents

### Functions

| [`deduplicate_subscribed_transactions`](#algokit_subscriber.subscription.deduplicate_subscribed_transactions)                           | Deduplicate subscribed transactions based on their ID.                                                                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`transaction_is_in_arc28_event_group`](#algokit_subscriber.subscription.transaction_is_in_arc28_event_group)                           | Check if a transaction is in an ARC-28 event group.                                                                                                                                                                  |
| [`has_emitted_matching_arc28_event`](#algokit_subscriber.subscription.has_emitted_matching_arc28_event)                                 | Check if a transaction has emitted a matching ARC-28 event.                                                                                                                                                          |
| [`extract_arc28_events`](#algokit_subscriber.subscription.extract_arc28_events)                                                         | Extract ARC-28 events from transaction logs.                                                                                                                                                                         |
| [`indexer_pre_filter`](#algokit_subscriber.subscription.indexer_pre_filter)                                                             | Create a pre-filter function for the Indexer client based on the subscription parameters.                                                                                                                            |
| [`indexer_pre_filter_in_memory`](#algokit_subscriber.subscription.indexer_pre_filter_in_memory)                                         | Create an in-memory pre-filter function based on the subscription parameters.                                                                                                                                        |
| [`get_method_selector_base64`](#algokit_subscriber.subscription.get_method_selector_base64)                                             | Get the base64-encoded method selector for a given method signature.                                                                                                                                                 |
| [`has_balance_change_match`](#algokit_subscriber.subscription.has_balance_change_match)                                                 | Check if there’s a match between the actual balance changes and the filtered balance changes.                                                                                                                        |
| [`get_subscribed_transactions`](#algokit_subscriber.subscription.get_subscribed_transactions)                                           | Executes a single pull/poll to subscribe to transactions on the configured Algorand<br/>blockchain for the given subscription context.                                                                               |
| [`process_extra_fields`](#algokit_subscriber.subscription.process_extra_fields)                                                         | Process extra fields for a transaction, including ARC-28 events and balance changes.                                                                                                                                 |
| [`extract_balance_changes_from_indexer_transaction`](#algokit_subscriber.subscription.extract_balance_changes_from_indexer_transaction) | Extract balance changes from an indexer transaction.                                                                                                                                                                 |
| [`get_filtered_indexer_transactions`](#algokit_subscriber.subscription.get_filtered_indexer_transactions)                               | Process an indexer transaction and return that transaction or any of its inner transactions<br/>that meet the indexer pre-filter requirements; patching up transaction ID and intra-round-offset on the way through. |
| [`get_indexer_inner_transactions`](#algokit_subscriber.subscription.get_indexer_inner_transactions)                                     | Recursively get inner transactions from an indexer transaction.                                                                                                                                                      |
| [`indexer_post_filter`](#algokit_subscriber.subscription.indexer_post_filter)                                                           | Create a post-filter function for indexer transactions based on the subscription parameters.                                                                                                                         |
| [`transaction_filter`](#algokit_subscriber.subscription.transaction_filter)                                                             | Create a filter function for transactions based on the subscription parameters.                                                                                                                                      |

### Data

| [`SearchForTransactions`](#algokit_subscriber.subscription.SearchForTransactions)   |    |
|-------------------------------------------------------------------------------------|----|

### API

### SearchForTransactions

None

### deduplicate_subscribed_transactions(txns: list[[algokit_subscriber.types.subscription.SubscribedTransaction](algokit_subscriber.types.subscription.md#algokit_subscriber.types.subscription.SubscribedTransaction)]) → list[[algokit_subscriber.types.subscription.SubscribedTransaction](algokit_subscriber.types.subscription.md#algokit_subscriber.types.subscription.SubscribedTransaction)]

Deduplicate subscribed transactions based on their ID.

* **Parameters:**
  **txns** – List of subscribed transactions
* **Returns:**
  Deduplicated list of subscribed transactions

### transaction_is_in_arc28_event_group(group: [algokit_subscriber.types.arc28.Arc28EventGroup](algokit_subscriber.types.arc28.md#algokit_subscriber.types.arc28.Arc28EventGroup), app_id: int, transaction: collections.abc.Callable[[], algokit_subscriber.types.indexer.TransactionResult]) → bool

Check if a transaction is in an ARC-28 event group.

* **Parameters:**
  * **group** – The ARC-28 event group to check against
  * **app_id** – The application ID of the transaction
  * **transaction** – A function that returns the transaction result
* **Returns:**
  True if the transaction is in the ARC-28 event group, False otherwise

### has_emitted_matching_arc28_event(logs: list[str], all_events: list[[algokit_subscriber.types.arc28.Arc28EventToProcess](algokit_subscriber.types.arc28.md#algokit_subscriber.types.arc28.Arc28EventToProcess)], event_groups: list[[algokit_subscriber.types.arc28.Arc28EventGroup](algokit_subscriber.types.arc28.md#algokit_subscriber.types.arc28.Arc28EventGroup)], event_filter: list[dict[str, str]], app_id: int, transaction: collections.abc.Callable[[], algokit_subscriber.types.indexer.TransactionResult]) → bool

Check if a transaction has emitted a matching ARC-28 event.

* **Parameters:**
  * **logs** – The transaction logs encoded as bas64 strings
  * **all_events** – All ARC-28 events to process
  * **event_groups** – All ARC-28 event groups
  * **event_filter** – The event filter to apply
  * **app_id** – The application ID
  * **transaction** – A function that returns the transaction result
* **Returns:**
  True if a matching ARC-28 event has been emitted, False otherwise

### extract_arc28_events(transaction_id: str, logs: list[bytes], events: list[[algokit_subscriber.types.arc28.Arc28EventToProcess](algokit_subscriber.types.arc28.md#algokit_subscriber.types.arc28.Arc28EventToProcess)], continue_on_error: collections.abc.Callable[[str], bool]) → list[[algokit_subscriber.types.arc28.EmittedArc28Event](algokit_subscriber.types.arc28.md#algokit_subscriber.types.arc28.EmittedArc28Event)]

Extract ARC-28 events from transaction logs.

* **Parameters:**
  * **transaction_id** – The ID of the transaction
  * **logs** – The transaction logs
  * **events** – The ARC-28 events to process
  * **continue_on_error** – A function that decides whether to continue on error for a given group name
* **Returns:**
  A list of emitted ARC-28 events, or an empty list if no events are found

### indexer_pre_filter(subscription: [algokit_subscriber.types.subscription.TransactionFilter](algokit_subscriber.types.subscription.md#algokit_subscriber.types.subscription.TransactionFilter), min_round: int, max_round: int) → dict[str, Any]

Create a pre-filter function for the Indexer client based on the subscription parameters.

* **Parameters:**
  * **subscription** – The transaction filter parameters
  * **min_round** – The minimum round number to search from
  * **max_round** – The maximum round number to search to
* **Returns:**
  A dictionary of pre-filter arguments for the Indexer client

### indexer_pre_filter_in_memory(subscription: [algokit_subscriber.types.subscription.TransactionFilter](algokit_subscriber.types.subscription.md#algokit_subscriber.types.subscription.TransactionFilter)) → collections.abc.Callable[[algokit_subscriber.types.indexer.TransactionResult], bool]

Create an in-memory pre-filter function based on the subscription parameters.

This is needed to overcome the problem that when indexer matches on an inner transaction,
it doesn’t return that inner transaction, it returns the parent. We need to re-run these
filters in-memory to identify the actual transaction(s) that were matched.

* **Parameters:**
  **subscription** – The transaction filter parameters
* **Returns:**
  A function that applies the pre-filter to a transaction dictionary

### get_method_selector_base64(method_signature: str) → str

Get the base64-encoded method selector for a given method signature.

* **Parameters:**
  **method_signature** – The method signature
* **Returns:**
  The base64-encoded method selector

### has_balance_change_match(transaction_balance_changes: list[[algokit_subscriber.types.subscription.BalanceChange](algokit_subscriber.types.subscription.md#algokit_subscriber.types.subscription.BalanceChange)], filtered_balance_changes: list[dict[str, Any]] | None) → bool

Check if there’s a match between the actual balance changes and the filtered balance changes.

* **Parameters:**
  * **transaction_balance_changes** – The actual balance changes in the transaction
  * **filtered_balance_changes** – The filtered balance changes to match against
* **Returns:**
  True if there’s a match, False otherwise

### get_subscribed_transactions(subscription: [algokit_subscriber.types.subscription.TransactionSubscriptionParams](algokit_subscriber.types.subscription.md#algokit_subscriber.types.subscription.TransactionSubscriptionParams), algod: algosdk.v2client.algod.AlgodClient, indexer: algosdk.v2client.indexer.IndexerClient | None = None) → [algokit_subscriber.types.subscription.TransactionSubscriptionResult](algokit_subscriber.types.subscription.md#algokit_subscriber.types.subscription.TransactionSubscriptionResult)

Executes a single pull/poll to subscribe to transactions on the configured Algorand
blockchain for the given subscription context.

* **Parameters:**
  * **subscription** – The subscription parameters
  * **algod** – The Algod client
  * **indexer** – The Indexer client (optional)
* **Returns:**
  The transaction subscription result

### process_extra_fields(transaction: algokit_subscriber.types.indexer.TransactionResult | [algokit_subscriber.types.subscription.SubscribedTransaction](algokit_subscriber.types.subscription.md#algokit_subscriber.types.subscription.SubscribedTransaction), arc28_events: list[[algokit_subscriber.types.arc28.Arc28EventToProcess](algokit_subscriber.types.arc28.md#algokit_subscriber.types.arc28.Arc28EventToProcess)], arc28_groups: list[[algokit_subscriber.types.arc28.Arc28EventGroup](algokit_subscriber.types.arc28.md#algokit_subscriber.types.arc28.Arc28EventGroup)]) → [algokit_subscriber.types.subscription.SubscribedTransaction](algokit_subscriber.types.subscription.md#algokit_subscriber.types.subscription.SubscribedTransaction)

Process extra fields for a transaction, including ARC-28 events and balance changes.

* **Parameters:**
  * **transaction** – The transaction to process
  * **arc28_events** – The list of ARC-28 events to process
  * **arc28_groups** – The list of ARC-28 event groups
* **Returns:**
  The processed transaction with extra fields

### extract_balance_changes_from_indexer_transaction(transaction: algokit_subscriber.types.indexer.TransactionResult) → list[[algokit_subscriber.types.subscription.BalanceChange](algokit_subscriber.types.subscription.md#algokit_subscriber.types.subscription.BalanceChange)]

Extract balance changes from an indexer transaction.

* **Parameters:**
  **transaction** – The indexer transaction
* **Returns:**
  A list of balance changes

### get_filtered_indexer_transactions(transaction: algokit_subscriber.types.indexer.TransactionResult, txn_filter: [algokit_subscriber.types.subscription.NamedTransactionFilter](algokit_subscriber.types.subscription.md#algokit_subscriber.types.subscription.NamedTransactionFilter)) → list[[algokit_subscriber.types.subscription.SubscribedTransaction](algokit_subscriber.types.subscription.md#algokit_subscriber.types.subscription.SubscribedTransaction)]

Process an indexer transaction and return that transaction or any of its inner transactions
that meet the indexer pre-filter requirements; patching up transaction ID and intra-round-offset on the way through.

* **Parameters:**
  * **transaction** – The indexer transaction to process
  * **txn_filter** – The named transaction filter to apply
* **Returns:**
  A list of filtered subscribed transactions

### get_indexer_inner_transactions(root: algokit_subscriber.types.indexer.TransactionResult, parent: algokit_subscriber.types.indexer.TransactionResult, offset: collections.abc.Callable) → list[[algokit_subscriber.types.subscription.SubscribedTransaction](algokit_subscriber.types.subscription.md#algokit_subscriber.types.subscription.SubscribedTransaction)]

Recursively get inner transactions from an indexer transaction.

* **Parameters:**
  * **root** – The root transaction
  * **parent** – The parent transaction
  * **offset** – A callable to get the parent offset
* **Returns:**
  A list of subscribed inner transactions

### indexer_post_filter(subscription: [algokit_subscriber.types.subscription.TransactionFilter](algokit_subscriber.types.subscription.md#algokit_subscriber.types.subscription.TransactionFilter), arc28_events: list[[algokit_subscriber.types.arc28.Arc28EventToProcess](algokit_subscriber.types.arc28.md#algokit_subscriber.types.arc28.Arc28EventToProcess)], arc28_event_groups: list[[algokit_subscriber.types.arc28.Arc28EventGroup](algokit_subscriber.types.arc28.md#algokit_subscriber.types.arc28.Arc28EventGroup)]) → collections.abc.Callable[[algokit_subscriber.types.indexer.TransactionResult], bool]

Create a post-filter function for indexer transactions based on the subscription parameters.

* **Parameters:**
  * **subscription** – The transaction filter parameters
  * **arc28_events** – The list of ARC-28 events to process
  * **arc28_event_groups** – The list of ARC-28 event groups
* **Returns:**
  A function that applies the post-filter to a transaction

### transaction_filter(subscription: [algokit_subscriber.types.subscription.TransactionFilter](algokit_subscriber.types.subscription.md#algokit_subscriber.types.subscription.TransactionFilter), arc28_events: list[[algokit_subscriber.types.arc28.Arc28EventToProcess](algokit_subscriber.types.arc28.md#algokit_subscriber.types.arc28.Arc28EventToProcess)], arc28_event_groups: list[[algokit_subscriber.types.arc28.Arc28EventGroup](algokit_subscriber.types.arc28.md#algokit_subscriber.types.arc28.Arc28EventGroup)]) → collections.abc.Callable[[[algokit_subscriber.types.block.TransactionInBlock](algokit_subscriber.types.block.md#algokit_subscriber.types.block.TransactionInBlock)], bool]

Create a filter function for transactions based on the subscription parameters.

* **Parameters:**
  * **subscription** – The transaction filter parameters
  * **arc28_events** – The list of ARC-28 events to process
  * **arc28_event_groups** – The list of ARC-28 event groups
* **Returns:**
  A function that applies the filter to a transaction in a block
