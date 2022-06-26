# BudgetElement


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budget_number** | **str** | Budgetnummer für das Detailobjekt. Die Budgetnummer ist eine numerische Bezeichnung im Rahmen der Gliederung des Haushaltsplans, die sich aus der Einzelplan-, Kapitel und Titelnummer zusammensetzt | 
**label** | **str** | Beschreibungstext für das Detailobjekt | 
**relative_to_parent_value** | **float** | Relativer Budgetwert zum Elternelement | 
**relative_value** | **float** | Relativer Budgetwert zum Gesamthaushalt des entsprechenden Jahres | 
**value** | **float** | tatsächlicher Budgetwert in € | 
**id** | **str** | ID, die sich aus der Budgetnummer generiert. Diese ID kann für konkrete Anfragen verwendet werden (query parameter &#39;id&#39;). ID ist nur in den Children-Objekten gefüllt. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


