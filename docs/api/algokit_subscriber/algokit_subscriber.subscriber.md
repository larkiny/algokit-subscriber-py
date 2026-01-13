# {py:mod}`algokit_subscriber.subscriber`

```{py:module} algokit_subscriber.subscriber
```

```{autodoc2-docstring} algokit_subscriber.subscriber
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`AlgorandSubscriber <algokit_subscriber.subscriber.AlgorandSubscriber>`
  - ```{autodoc2-docstring} algokit_subscriber.subscriber.AlgorandSubscriber
    :summary:
    ```
````

### API

`````{py:class} AlgorandSubscriber(config: algokit_subscriber.types.subscription.AlgorandSubscriberConfig, algod_client: algosdk.v2client.algod.AlgodClient, indexer_client: algosdk.v2client.indexer.IndexerClient | None = None)
:canonical: algokit_subscriber.subscriber.AlgorandSubscriber

```{autodoc2-docstring} algokit_subscriber.subscriber.AlgorandSubscriber
```

```{rubric} Initialization
```

```{autodoc2-docstring} algokit_subscriber.subscriber.AlgorandSubscriber.__init__
```

````{py:method} default_error_handler(error: typing.Any, _str: str | None = None) -> None
:canonical: algokit_subscriber.subscriber.AlgorandSubscriber.default_error_handler

```{autodoc2-docstring} algokit_subscriber.subscriber.AlgorandSubscriber.default_error_handler
```

````

````{py:method} poll_once() -> algokit_subscriber.types.subscription.TransactionSubscriptionResult
:canonical: algokit_subscriber.subscriber.AlgorandSubscriber.poll_once

```{autodoc2-docstring} algokit_subscriber.subscriber.AlgorandSubscriber.poll_once
```

````

````{py:method} start(inspect: collections.abc.Callable | None = None, *, suppress_log: bool = False) -> None
:canonical: algokit_subscriber.subscriber.AlgorandSubscriber.start

```{autodoc2-docstring} algokit_subscriber.subscriber.AlgorandSubscriber.start
```

````

````{py:method} stop(reason: str | None = None) -> None
:canonical: algokit_subscriber.subscriber.AlgorandSubscriber.stop

```{autodoc2-docstring} algokit_subscriber.subscriber.AlgorandSubscriber.stop
```

````

````{py:method} on(filter_name: str, listener: algokit_subscriber.types.event_emitter.EventListener) -> algokit_subscriber.subscriber.AlgorandSubscriber
:canonical: algokit_subscriber.subscriber.AlgorandSubscriber.on

```{autodoc2-docstring} algokit_subscriber.subscriber.AlgorandSubscriber.on
```

````

````{py:method} on_batch(filter_name: str, listener: algokit_subscriber.types.event_emitter.EventListener) -> algokit_subscriber.subscriber.AlgorandSubscriber
:canonical: algokit_subscriber.subscriber.AlgorandSubscriber.on_batch

```{autodoc2-docstring} algokit_subscriber.subscriber.AlgorandSubscriber.on_batch
```

````

````{py:method} on_before_poll(listener: algokit_subscriber.types.event_emitter.EventListener) -> algokit_subscriber.subscriber.AlgorandSubscriber
:canonical: algokit_subscriber.subscriber.AlgorandSubscriber.on_before_poll

```{autodoc2-docstring} algokit_subscriber.subscriber.AlgorandSubscriber.on_before_poll
```

````

````{py:method} on_poll(listener: algokit_subscriber.types.event_emitter.EventListener) -> algokit_subscriber.subscriber.AlgorandSubscriber
:canonical: algokit_subscriber.subscriber.AlgorandSubscriber.on_poll

```{autodoc2-docstring} algokit_subscriber.subscriber.AlgorandSubscriber.on_poll
```

````

````{py:method} on_error(listener: algokit_subscriber.types.event_emitter.EventListener) -> algokit_subscriber.subscriber.AlgorandSubscriber
:canonical: algokit_subscriber.subscriber.AlgorandSubscriber.on_error

```{autodoc2-docstring} algokit_subscriber.subscriber.AlgorandSubscriber.on_error
```

````

`````
