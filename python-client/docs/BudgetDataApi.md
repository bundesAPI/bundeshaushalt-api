# bundeshaushalt.BudgetDataApi

All URIs are relative to *https://bundeshaushalt.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**budget_data**](BudgetDataApi.md#budget_data) | **GET** /internalapi/budgetData | Anfrage von Budgetdaten des Bundeshaushalts.


# **budget_data**
> BudgetDataResponse budget_data(year, account)

Anfrage von Budgetdaten des Bundeshaushalts.

Haupteinstiegspunkt für alle Anfragen.

### Example


```python
import time
from deutschland import bundeshaushalt
from deutschland.bundeshaushalt.api import budget_data_api
from deutschland.bundeshaushalt.model.bad_request import BadRequest
from deutschland.bundeshaushalt.model.budget_data_response import BudgetDataResponse
from pprint import pprint
# Defining the host is optional and defaults to https://bundeshaushalt.de
# See configuration.py for a list of all supported configuration parameters.
configuration = bundeshaushalt.Configuration(
    host = "https://bundeshaushalt.de"
)


# Enter a context with an instance of the API client
with bundeshaushalt.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = budget_data_api.BudgetDataApi(api_client)
    year = 2021 # int | Haushaltsjahr
    account = "expenses" # str | <b>income</b>: Einnahmen. Die Einnahmen des Bundes setzen sich aus Steuern, sonstigen Einnahmen und Krediten zusammen.<br><b>expenses</b>: Ausgaben. Der größte Teil der Ausgaben wird für Sozialausgaben geleistet. Weitere große Ausgabeposten sind die Ausgabebereiche Verteidigung, Verkehrs- und Nachrichtenwesen und auch Bildung und Forschung.
    quota = "actual" # str | <b>target</b>: Sollwerte <i>(default)</i><br><b>actual</b>: Istwerte. (optional)
    unit = "function" # str | <b>single</b>: Einzelplan. <i>(default)</i><br><b>function</b>: Funktion.<br><b>group</b>: Gruppe. (optional)
    id = "090168301" # str | ID, die sich aus der Budgetnummer ergibt. Die Budgetnummer ist eine numerische Bezeichnung im Rahmen der Gliederung des Haushaltsplans, die sich aus der Einzelplan-, Kapitel und Titelnummer zusammensetzt. Gruppen-IDs starten mit 'G-', Funktions-IDs mit 'F-' (optional)

    # example passing only required values which don't have defaults set
    try:
        # Anfrage von Budgetdaten des Bundeshaushalts.
        api_response = api_instance.budget_data(year, account)
        pprint(api_response)
    except bundeshaushalt.ApiException as e:
        print("Exception when calling BudgetDataApi->budget_data: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Anfrage von Budgetdaten des Bundeshaushalts.
        api_response = api_instance.budget_data(year, account, quota=quota, unit=unit, id=id)
        pprint(api_response)
    except bundeshaushalt.ApiException as e:
        print("Exception when calling BudgetDataApi->budget_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Haushaltsjahr |
 **account** | **str**| &lt;b&gt;income&lt;/b&gt;: Einnahmen. Die Einnahmen des Bundes setzen sich aus Steuern, sonstigen Einnahmen und Krediten zusammen.&lt;br&gt;&lt;b&gt;expenses&lt;/b&gt;: Ausgaben. Der größte Teil der Ausgaben wird für Sozialausgaben geleistet. Weitere große Ausgabeposten sind die Ausgabebereiche Verteidigung, Verkehrs- und Nachrichtenwesen und auch Bildung und Forschung. |
 **quota** | **str**| &lt;b&gt;target&lt;/b&gt;: Sollwerte &lt;i&gt;(default)&lt;/i&gt;&lt;br&gt;&lt;b&gt;actual&lt;/b&gt;: Istwerte. | [optional]
 **unit** | **str**| &lt;b&gt;single&lt;/b&gt;: Einzelplan. &lt;i&gt;(default)&lt;/i&gt;&lt;br&gt;&lt;b&gt;function&lt;/b&gt;: Funktion.&lt;br&gt;&lt;b&gt;group&lt;/b&gt;: Gruppe. | [optional]
 **id** | **str**| ID, die sich aus der Budgetnummer ergibt. Die Budgetnummer ist eine numerische Bezeichnung im Rahmen der Gliederung des Haushaltsplans, die sich aus der Einzelplan-, Kapitel und Titelnummer zusammensetzt. Gruppen-IDs starten mit &#39;G-&#39;, Funktions-IDs mit &#39;F-&#39; | [optional]

### Return type

[**BudgetDataResponse**](BudgetDataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

