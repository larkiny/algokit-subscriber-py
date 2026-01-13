---
title: algokit_subscriber.subscriber
---

# [`algokit_subscriber.subscriber`](#module-algokit_subscriber.subscriber)

## Module Contents

### Classes

| [`AlgorandSubscriber`](#algokit_subscriber.subscriber.AlgorandSubscriber)   | A subscriber for Algorand transactions.   |
|-----------------------------------------------------------------------------|-------------------------------------------|

### API

### *class* AlgorandSubscriber(config: [algokit_subscriber.types.subscription.AlgorandSubscriberConfig](algokit_subscriber.types.subscription.md#algokit_subscriber.types.subscription.AlgorandSubscriberConfig), algod_client: algosdk.v2client.algod.AlgodClient, indexer_client: algosdk.v2client.indexer.IndexerClient | None = None)

A subscriber for Algorand transactions.

### Initialization

Create a new `AlgorandSubscriber`.

* **Parameters:**
  * **config** – The subscriber configuration
  * **algod_client** – An algod client
  * **indexer_client** – An (optional) indexer client; only needed if `subscription.syncBehaviour` is `catchup-with-indexer`

#### default_error_handler(error: Any, \_str: str | None = None) → None

#### poll_once() → [algokit_subscriber.types.subscription.TransactionSubscriptionResult](algokit_subscriber.types.subscription.md#algokit_subscriber.types.subscription.TransactionSubscriptionResult)

Execute a single subscription poll.

#### start(inspect: collections.abc.Callable | None = None, , suppress_log: bool = False) → None

Start the subscriber in a loop until `stop` is called.

This is useful when running in the context of a long-running process / container.

If you want to inspect or log what happens under the covers you can pass in an `inspect` callable that will be called for each poll.

#### stop(reason: str | None = None) → None

#### on(filter_name: str, listener: algokit_subscriber.types.event_emitter.EventListener) → [algokit_subscriber.subscriber.AlgorandSubscriber](#algokit_subscriber.subscriber.AlgorandSubscriber)

Register an event handler to run on every subscribed transaction matching the given filter name.

#### on_batch(filter_name: str, listener: algokit_subscriber.types.event_emitter.EventListener) → [algokit_subscriber.subscriber.AlgorandSubscriber](#algokit_subscriber.subscriber.AlgorandSubscriber)

Register an event handler to run on all subscribed transactions matching the given filter name
for each subscription poll.

#### on_before_poll(listener: algokit_subscriber.types.event_emitter.EventListener) → [algokit_subscriber.subscriber.AlgorandSubscriber](#algokit_subscriber.subscriber.AlgorandSubscriber)

Register an event handler to run before each subscription poll.

#### on_poll(listener: algokit_subscriber.types.event_emitter.EventListener) → [algokit_subscriber.subscriber.AlgorandSubscriber](#algokit_subscriber.subscriber.AlgorandSubscriber)

Register an event handler to run after each subscription poll.

#### on_error(listener: algokit_subscriber.types.event_emitter.EventListener) → [algokit_subscriber.subscriber.AlgorandSubscriber](#algokit_subscriber.subscriber.AlgorandSubscriber)

Register an event handler to run when an error occurs.
