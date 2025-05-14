# CreateProductsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **int** | Channel ID through which the request is made | 
**device_id** | **str** | Unique device identifier | [optional] 
**device_type** | **str** | Type of the device | [optional] 
**user_id** | **int** | User ID making the request | [optional] 
**token** | **str** | Session Token | [optional] 
**create_product_requests** | [**List[CreateProductRequestBean]**](CreateProductRequestBean.md) |  | [optional] 

## Example

```python
from product_api_client.models.create_products_request import CreateProductsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProductsRequest from a JSON string
create_products_request_instance = CreateProductsRequest.from_json(json)
# print the JSON string representation of the object
print(CreateProductsRequest.to_json())

# convert the object into a dict
create_products_request_dict = create_products_request_instance.to_dict()
# create an instance of CreateProductsRequest from a dict
create_products_request_from_dict = CreateProductsRequest.from_dict(create_products_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


