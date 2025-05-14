# CreateProductResponseBean


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**product_id** | **str** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from product_api_client.models.create_product_response_bean import CreateProductResponseBean

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProductResponseBean from a JSON string
create_product_response_bean_instance = CreateProductResponseBean.from_json(json)
# print the JSON string representation of the object
print(CreateProductResponseBean.to_json())

# convert the object into a dict
create_product_response_bean_dict = create_product_response_bean_instance.to_dict()
# create an instance of CreateProductResponseBean from a dict
create_product_response_bean_from_dict = CreateProductResponseBean.from_dict(create_product_response_bean_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


