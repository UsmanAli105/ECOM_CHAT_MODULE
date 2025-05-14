# UpdateOrderStatusResponseBean


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from order_api_client.models.update_order_status_response_bean import UpdateOrderStatusResponseBean

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOrderStatusResponseBean from a JSON string
update_order_status_response_bean_instance = UpdateOrderStatusResponseBean.from_json(json)
# print the JSON string representation of the object
print(UpdateOrderStatusResponseBean.to_json())

# convert the object into a dict
update_order_status_response_bean_dict = update_order_status_response_bean_instance.to_dict()
# create an instance of UpdateOrderStatusResponseBean from a dict
update_order_status_response_bean_from_dict = UpdateOrderStatusResponseBean.from_dict(update_order_status_response_bean_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


