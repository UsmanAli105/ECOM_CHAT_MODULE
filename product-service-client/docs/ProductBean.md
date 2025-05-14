# ProductBean


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**image_path** | **str** |  | [optional] 
**price** | **float** |  | [optional] 
**stock** | **int** |  | [optional] 
**category** | **str** |  | [optional] 
**brand** | **str** |  | [optional] 
**rating** | **int** |  | [optional] 

## Example

```python
from product_api_client.models.product_bean import ProductBean

# TODO update the JSON string below
json = "{}"
# create an instance of ProductBean from a JSON string
product_bean_instance = ProductBean.from_json(json)
# print the JSON string representation of the object
print(ProductBean.to_json())

# convert the object into a dict
product_bean_dict = product_bean_instance.to_dict()
# create an instance of ProductBean from a dict
product_bean_from_dict = ProductBean.from_dict(product_bean_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


