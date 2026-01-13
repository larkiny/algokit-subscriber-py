---
title: algokit_subscriber.types.event_emitter
---

# [`algokit_subscriber.types.event_emitter`](#module-algokit_subscriber.types.event_emitter)

## Module Contents

### Classes

| [`EventEmitter`](#algokit_subscriber.types.event_emitter.EventEmitter)   | A simple event emitter that allows for the registration of event listeners and the<br/>emission of events to those listeners.   |
|--------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|

### Data

| [`EventListener`](#algokit_subscriber.types.event_emitter.EventListener)   | A function that takes a SubscribedTransaction and the event name.   |
|----------------------------------------------------------------------------|---------------------------------------------------------------------|

### API

### EventListener

None

A function that takes a SubscribedTransaction and the event name.

### *class* EventEmitter

A simple event emitter that allows for the registration of event listeners and the
emission of events to those listeners.

### Initialization

#### emit(event_name: str, event: Any) → None

Emits an event to all listeners registered for the event name.

#### on(event_name: str, listener: algokit_subscriber.types.event_emitter.EventListener) → [algokit_subscriber.types.event_emitter.EventEmitter](#algokit_subscriber.types.event_emitter.EventEmitter)

Registers a listener for the given event name.

#### once(event_name: str, listener: algokit_subscriber.types.event_emitter.EventListener) → [algokit_subscriber.types.event_emitter.EventEmitter](#algokit_subscriber.types.event_emitter.EventEmitter)

Registers a listener for the given event name that will only be called once.

#### remove_listener(event_name: str, listener: algokit_subscriber.types.event_emitter.EventListener) → [algokit_subscriber.types.event_emitter.EventEmitter](#algokit_subscriber.types.event_emitter.EventEmitter)

Removes a listener for the given event name.

#### off

None
