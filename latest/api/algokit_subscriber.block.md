---
title: algokit_subscriber.block
---

# [`algokit_subscriber.block`](#module-algokit_subscriber.block)

## Module Contents

### Functions

| [`block_response_to_block_data`](#algokit_subscriber.block.block_response_to_block_data)   |                                                                          |
|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| [`get_blocks_bulk`](#algokit_subscriber.block.get_blocks_bulk)                             | Retrieves blocks in bulk (30 at a time) between the given round numbers. |

### API

### block_response_to_block_data(response: bytes) → [algokit_subscriber.types.block.BlockData](algokit_subscriber.types.block.md#algokit_subscriber.types.block.BlockData)

### get_blocks_bulk(context: dict[str, int], client: algosdk.v2client.algod.AlgodClient) → list[[algokit_subscriber.types.block.BlockData](algokit_subscriber.types.block.md#algokit_subscriber.types.block.BlockData)]

Retrieves blocks in bulk (30 at a time) between the given round numbers.

* **Parameters:**
  * **context** – A dictionary containing ‘startRound’ and ‘maxRound’
  * **client** – The algod client
* **Returns:**
  The blocks
