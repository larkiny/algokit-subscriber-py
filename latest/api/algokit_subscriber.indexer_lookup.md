---
title: algokit_subscriber.indexer_lookup
---

# [`algokit_subscriber.indexer_lookup`](#module-algokit_subscriber.indexer_lookup)

## Module Contents

### Functions

| [`transaction`](#algokit_subscriber.indexer_lookup.transaction)                                                                     | Looks up a transaction by ID using Indexer.                                                                 |
|-------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| [`lookup_account_by_address`](#algokit_subscriber.indexer_lookup.lookup_account_by_address)                                         | Looks up an account by address using Indexer.                                                               |
| [`lookup_account_created_application_by_address`](#algokit_subscriber.indexer_lookup.lookup_account_created_application_by_address) | Looks up applications that were created by the given address; will automatically paginate through all data. |
| [`lookup_asset_holdings`](#algokit_subscriber.indexer_lookup.lookup_asset_holdings)                                                 | Looks up asset holdings for the given asset; will automatically paginate through all data.                  |
| [`search_transactions`](#algokit_subscriber.indexer_lookup.search_transactions)                                                     | Allows transactions to be searched for the given criteria.                                                  |
| [`execute_paginated_request`](#algokit_subscriber.indexer_lookup.execute_paginated_request)                                         | Executes a paginated request and returns all results.                                                       |

### Data

| [`DEFAULT_INDEXER_MAX_API_RESOURCES_PER_ACCOUNT`](#algokit_subscriber.indexer_lookup.DEFAULT_INDEXER_MAX_API_RESOURCES_PER_ACCOUNT)   |    |
|---------------------------------------------------------------------------------------------------------------------------------------|----|

### API

### DEFAULT_INDEXER_MAX_API_RESOURCES_PER_ACCOUNT

1000

### transaction(transaction_id: str, indexer: algosdk.v2client.indexer.IndexerClient) → algokit_subscriber.types.indexer.TransactionLookupResult

Looks up a transaction by ID using Indexer.

### lookup_account_by_address(account_address: str, indexer: algosdk.v2client.indexer.IndexerClient) → algokit_subscriber.types.indexer.AccountLookupResult

Looks up an account by address using Indexer.

### lookup_account_created_application_by_address(indexer: algosdk.v2client.indexer.IndexerClient, address: str, get_all: bool | None = None, pagination_limit: int | None = None) → list[algokit_subscriber.types.indexer.ApplicationResult]

Looks up applications that were created by the given address; will automatically paginate through all data.

### lookup_asset_holdings(indexer: algosdk.v2client.indexer.IndexerClient, asset_id: int, options: algokit_subscriber.types.indexer.LookupAssetHoldingsOptions | None = None, pagination_limit: int | None = None) → list[algokit_subscriber.types.indexer.MiniAssetHolding]

Looks up asset holdings for the given asset; will automatically paginate through all data.

### search_transactions(indexer: algosdk.v2client.indexer.IndexerClient, search_criteria: dict[str, Any], pagination_limit: int | None = None) → algokit_subscriber.types.indexer.TransactionSearchResults

Allows transactions to be searched for the given criteria.

### execute_paginated_request(method: collections.abc.Callable, extract_items: collections.abc.Callable[[Any], list[Any]], build_request: collections.abc.Callable[[str | None], dict[str, Any]]) → list[Any]

Executes a paginated request and returns all results.
