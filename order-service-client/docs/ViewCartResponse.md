# ViewCartResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**Status**](Status.md) |  | [optional] 
**view_cart_bean** | [**ViewCartBean**](ViewCartBean.md) |  | [optional] 

## Example

```python
from order_api_client.models.view_cart_response import ViewCartResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ViewCartResponse from a JSON string
view_cart_response_instance = ViewCartResponse.from_json(json)
# print the JSON string representation of the object
print(ViewCartResponse.to_json())

# convert the object into a dict
view_cart_response_dict = view_cart_response_instance.to_dict()
# create an instance of ViewCartResponse from a dict
view_cart_response_from_dict = ViewCartResponse.from_dict(view_cart_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


