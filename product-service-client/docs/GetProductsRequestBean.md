# GetProductsRequestBean


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**product_ids** | **List[str]** |  | [optional] 
**category_id** | **int** |  | [optional] 
**brand_id** | **int** |  | [optional] 
**min_price** | **float** |  | [optional] 
**max_price** | **float** |  | [optional] 
**min_rating** | **int** |  | [optional] 

## Example

```python
from product_api_client.models.get_products_request_bean import GetProductsRequestBean

# TODO update the JSON string below
json = "{}"
# create an instance of GetProductsRequestBean from a JSON string
get_products_request_bean_instance = GetProductsRequestBean.from_json(json)
# print the JSON string representation of the object
print(GetProductsRequestBean.to_json())

# convert the object into a dict
get_products_request_bean_dict = get_products_request_bean_instance.to_dict()
# create an instance of GetProductsRequestBean from a dict
get_products_request_bean_from_dict = GetProductsRequestBean.from_dict(get_products_request_bean_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


