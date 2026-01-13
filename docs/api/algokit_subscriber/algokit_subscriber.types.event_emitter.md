# {py:mod}`algokit_subscriber.types.event_emitter`

```{py:module} algokit_subscriber.types.event_emitter
```

```{autodoc2-docstring} algokit_subscriber.types.event_emitter
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`EventEmitter <algokit_subscriber.types.event_emitter.EventEmitter>`
  - ```{autodoc2-docstring} algokit_subscriber.types.event_emitter.EventEmitter
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`EventListener <algokit_subscriber.types.event_emitter.EventListener>`
  - ```{autodoc2-docstring} algokit_subscriber.types.event_emitter.EventListener
    :summary:
    ```
````

### API

````{py:data} EventListener
:canonical: algokit_subscriber.types.event_emitter.EventListener
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.event_emitter.EventListener
```

````

`````{py:class} EventEmitter()
:canonical: algokit_subscriber.types.event_emitter.EventEmitter

```{autodoc2-docstring} algokit_subscriber.types.event_emitter.EventEmitter
```

```{rubric} Initialization
```

```{autodoc2-docstring} algokit_subscriber.types.event_emitter.EventEmitter.__init__
```

````{py:method} emit(event_name: str, event: typing.Any) -> None
:canonical: algokit_subscriber.types.event_emitter.EventEmitter.emit

```{autodoc2-docstring} algokit_subscriber.types.event_emitter.EventEmitter.emit
```

````

````{py:method} on(event_name: str, listener: algokit_subscriber.types.event_emitter.EventListener) -> algokit_subscriber.types.event_emitter.EventEmitter
:canonical: algokit_subscriber.types.event_emitter.EventEmitter.on

```{autodoc2-docstring} algokit_subscriber.types.event_emitter.EventEmitter.on
```

````

````{py:method} once(event_name: str, listener: algokit_subscriber.types.event_emitter.EventListener) -> algokit_subscriber.types.event_emitter.EventEmitter
:canonical: algokit_subscriber.types.event_emitter.EventEmitter.once

```{autodoc2-docstring} algokit_subscriber.types.event_emitter.EventEmitter.once
```

````

````{py:method} remove_listener(event_name: str, listener: algokit_subscriber.types.event_emitter.EventListener) -> algokit_subscriber.types.event_emitter.EventEmitter
:canonical: algokit_subscriber.types.event_emitter.EventEmitter.remove_listener

```{autodoc2-docstring} algokit_subscriber.types.event_emitter.EventEmitter.remove_listener
```

````

````{py:attribute} off
:canonical: algokit_subscriber.types.event_emitter.EventEmitter.off
:value: >
   None

```{autodoc2-docstring} algokit_subscriber.types.event_emitter.EventEmitter.off
```

````

`````
