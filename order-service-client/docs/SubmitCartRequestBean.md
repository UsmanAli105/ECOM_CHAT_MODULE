# SubmitCartRequestBean


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cash_on_delivery** | **bool** |  | [optional] 
**agree_terms** | **bool** |  | [optional] 
**address** | [**UserAddressBean**](UserAddressBean.md) |  | [optional] 
**submit** | **bool** |  | [optional] 

## Example

```python
from order_api_client.models.submit_cart_request_bean import SubmitCartRequestBean

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitCartRequestBean from a JSON string
submit_cart_request_bean_instance = SubmitCartRequestBean.from_json(json)
# print the JSON string representation of the object
print(SubmitCartRequestBean.to_json())

# convert the object into a dict
submit_cart_request_bean_dict = submit_cart_request_bean_instance.to_dict()
# create an instance of SubmitCartRequestBean from a dict
submit_cart_request_bean_from_dict = SubmitCartRequestBean.from_dict(submit_cart_request_bean_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


