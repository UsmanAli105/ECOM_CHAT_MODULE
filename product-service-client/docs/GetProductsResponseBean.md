# GetProductsResponseBean


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**products** | [**List[ProductBean]**](ProductBean.md) |  | [optional] 

## Example

```python
from product_api_client.models.get_products_response_bean import GetProductsResponseBean

# TODO update the JSON string below
json = "{}"
# create an instance of GetProductsResponseBean from a JSON string
get_products_response_bean_instance = GetProductsResponseBean.from_json(json)
# print the JSON string representation of the object
print(GetProductsResponseBean.to_json())

# convert the object into a dict
get_products_response_bean_dict = get_products_response_bean_instance.to_dict()
# create an instance of GetProductsResponseBean from a dict
get_products_response_bean_from_dict = GetProductsResponseBean.from_dict(get_products_response_bean_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


