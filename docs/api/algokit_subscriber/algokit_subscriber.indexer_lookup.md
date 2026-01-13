# {py:mod}`algokit_subscriber.indexer_lookup`

```{py:module} algokit_subscriber.indexer_lookup
```

```{autodoc2-docstring} algokit_subscriber.indexer_lookup
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`transaction <algokit_subscriber.indexer_lookup.transaction>`
  - ```{autodoc2-docstring} algokit_subscriber.indexer_lookup.transaction
    :summary:
    ```
* - {py:obj}`lookup_account_by_address <algokit_subscriber.indexer_lookup.lookup_account_by_address>`
  - ```{autodoc2-docstring} algokit_subscriber.indexer_lookup.lookup_account_by_address
    :summary:
    ```
* - {py:obj}`lookup_account_created_application_by_address <algokit_subscriber.indexer_lookup.lookup_account_created_application_by_address>`
  - ```{autodoc2-docstring} algokit_subscriber.indexer_lookup.lookup_account_created_application_by_address
    :summary:
    ```
* - {py:obj}`lookup_asset_holdings <algokit_subscriber.indexer_lookup.lookup_asset_holdings>`
  - ```{autodoc2-docstring} algokit_subscriber.indexer_lookup.lookup_asset_holdings
    :summary:
    ```
* - {py:obj}`search_transactions <algokit_subscriber.indexer_lookup.search_transactions>`
  - ```{autodoc2-docstring} algokit_subscriber.indexer_lookup.search_transactions
    :summary:
    ```
* - {py:obj}`execute_paginated_request <algokit_subscriber.indexer_lookup.execute_paginated_request>`
  - ```{autodoc2-docstring} algokit_subscriber.indexer_lookup.execute_paginated_request
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`DEFAULT_INDEXER_MAX_API_RESOURCES_PER_ACCOUNT <algokit_subscriber.indexer_lookup.DEFAULT_INDEXER_MAX_API_RESOURCES_PER_ACCOUNT>`
  - ```{autodoc2-docstring} algokit_subscriber.indexer_lookup.DEFAULT_INDEXER_MAX_API_RESOURCES_PER_ACCOUNT
    :summary:
    ```
````

### API

````{py:data} DEFAULT_INDEXER_MAX_API_RESOURCES_PER_ACCOUNT
:canonical: algokit_subscriber.indexer_lookup.DEFAULT_INDEXER_MAX_API_RESOURCES_PER_ACCOUNT
:value: >
   1000

```{autodoc2-docstring} algokit_subscriber.indexer_lookup.DEFAULT_INDEXER_MAX_API_RESOURCES_PER_ACCOUNT
```

````

````{py:function} transaction(transaction_id: str, indexer: algosdk.v2client.indexer.IndexerClient) -> algokit_subscriber.types.indexer.TransactionLookupResult
:canonical: algokit_subscriber.indexer_lookup.transaction

```{autodoc2-docstring} algokit_subscriber.indexer_lookup.transaction
```
````

````{py:function} lookup_account_by_address(account_address: str, indexer: algosdk.v2client.indexer.IndexerClient) -> algokit_subscriber.types.indexer.AccountLookupResult
:canonical: algokit_subscriber.indexer_lookup.lookup_account_by_address

```{autodoc2-docstring} algokit_subscriber.indexer_lookup.lookup_account_by_address
```
````

````{py:function} lookup_account_created_application_by_address(indexer: algosdk.v2client.indexer.IndexerClient, address: str, get_all: bool | None = None, pagination_limit: int | None = None) -> list[algokit_subscriber.types.indexer.ApplicationResult]
:canonical: algokit_subscriber.indexer_lookup.lookup_account_created_application_by_address

```{autodoc2-docstring} algokit_subscriber.indexer_lookup.lookup_account_created_application_by_address
```
````

````{py:function} lookup_asset_holdings(indexer: algosdk.v2client.indexer.IndexerClient, asset_id: int, options: algokit_subscriber.types.indexer.LookupAssetHoldingsOptions | None = None, pagination_limit: int | None = None) -> list[algokit_subscriber.types.indexer.MiniAssetHolding]
:canonical: algokit_subscriber.indexer_lookup.lookup_asset_holdings

```{autodoc2-docstring} algokit_subscriber.indexer_lookup.lookup_asset_holdings
```
````

````{py:function} search_transactions(indexer: algosdk.v2client.indexer.IndexerClient, search_criteria: dict[str, typing.Any], pagination_limit: int | None = None) -> algokit_subscriber.types.indexer.TransactionSearchResults
:canonical: algokit_subscriber.indexer_lookup.search_transactions

```{autodoc2-docstring} algokit_subscriber.indexer_lookup.search_transactions
```
````

````{py:function} execute_paginated_request(method: collections.abc.Callable, extract_items: collections.abc.Callable[[typing.Any], list[typing.Any]], build_request: collections.abc.Callable[[str | None], dict[str, typing.Any]]) -> list[typing.Any]
:canonical: algokit_subscriber.indexer_lookup.execute_paginated_request

```{autodoc2-docstring} algokit_subscriber.indexer_lookup.execute_paginated_request
```
````
