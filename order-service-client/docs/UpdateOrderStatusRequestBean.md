# UpdateOrderStatusRequestBean


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**order_id** | **int** |  | 
**status_id** | **int** |  | 

## Example

```python
from order_api_client.models.update_order_status_request_bean import UpdateOrderStatusRequestBean

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOrderStatusRequestBean from a JSON string
update_order_status_request_bean_instance = UpdateOrderStatusRequestBean.from_json(json)
# print the JSON string representation of the object
print(UpdateOrderStatusRequestBean.to_json())

# convert the object into a dict
update_order_status_request_bean_dict = update_order_status_request_bean_instance.to_dict()
# create an instance of UpdateOrderStatusRequestBean from a dict
update_order_status_request_bean_from_dict = UpdateOrderStatusRequestBean.from_dict(update_order_status_request_bean_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


