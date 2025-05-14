# SubmitCartResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**Status**](Status.md) |  | [optional] 
**submit_cart_response_bean** | [**SubmitCartResponseBean**](SubmitCartResponseBean.md) |  | [optional] 

## Example

```python
from order_api_client.models.submit_cart_response import SubmitCartResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitCartResponse from a JSON string
submit_cart_response_instance = SubmitCartResponse.from_json(json)
# print the JSON string representation of the object
print(SubmitCartResponse.to_json())

# convert the object into a dict
submit_cart_response_dict = submit_cart_response_instance.to_dict()
# create an instance of SubmitCartResponse from a dict
submit_cart_response_from_dict = SubmitCartResponse.from_dict(submit_cart_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


