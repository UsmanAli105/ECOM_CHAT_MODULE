# CreateProductRequestBean


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brand_id** | **int** |  | [optional] 
**category_id** | **int** |  | [optional] 
**product_name** | **str** |  | [optional] 
**product_description** | **str** |  | [optional] 
**image_path** | **str** |  | [optional] 
**base_price** | **float** |  | [optional] 
**gst** | **float** |  | [optional] 

## Example

```python
from product_api_client.models.create_product_request_bean import CreateProductRequestBean

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProductRequestBean from a JSON string
create_product_request_bean_instance = CreateProductRequestBean.from_json(json)
# print the JSON string representation of the object
print(CreateProductRequestBean.to_json())

# convert the object into a dict
create_product_request_bean_dict = create_product_request_bean_instance.to_dict()
# create an instance of CreateProductRequestBean from a dict
create_product_request_bean_from_dict = CreateProductRequestBean.from_dict(create_product_request_bean_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


