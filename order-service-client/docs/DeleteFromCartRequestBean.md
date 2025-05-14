# DeleteFromCartRequestBean


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** |  | [optional] 

## Example

```python
from order_api_client.models.delete_from_cart_request_bean import DeleteFromCartRequestBean

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteFromCartRequestBean from a JSON string
delete_from_cart_request_bean_instance = DeleteFromCartRequestBean.from_json(json)
# print the JSON string representation of the object
print(DeleteFromCartRequestBean.to_json())

# convert the object into a dict
delete_from_cart_request_bean_dict = delete_from_cart_request_bean_instance.to_dict()
# create an instance of DeleteFromCartRequestBean from a dict
delete_from_cart_request_bean_from_dict = DeleteFromCartRequestBean.from_dict(delete_from_cart_request_bean_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


