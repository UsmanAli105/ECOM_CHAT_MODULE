# UserAddressBean


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**house** | **str** |  | [optional] 
**street** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**zip** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**email** | **str** |  | [optional] 

## Example

```python
from order_api_client.models.user_address_bean import UserAddressBean

# TODO update the JSON string below
json = "{}"
# create an instance of UserAddressBean from a JSON string
user_address_bean_instance = UserAddressBean.from_json(json)
# print the JSON string representation of the object
print(UserAddressBean.to_json())

# convert the object into a dict
user_address_bean_dict = user_address_bean_instance.to_dict()
# create an instance of UserAddressBean from a dict
user_address_bean_from_dict = UserAddressBean.from_dict(user_address_bean_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


