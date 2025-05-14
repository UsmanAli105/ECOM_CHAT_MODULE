# DeleteFromCartResponseBean


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from order_api_client.models.delete_from_cart_response_bean import DeleteFromCartResponseBean

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteFromCartResponseBean from a JSON string
delete_from_cart_response_bean_instance = DeleteFromCartResponseBean.from_json(json)
# print the JSON string representation of the object
print(DeleteFromCartResponseBean.to_json())

# convert the object into a dict
delete_from_cart_response_bean_dict = delete_from_cart_response_bean_instance.to_dict()
# create an instance of DeleteFromCartResponseBean from a dict
delete_from_cart_response_bean_from_dict = DeleteFromCartResponseBean.from_dict(delete_from_cart_response_bean_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


