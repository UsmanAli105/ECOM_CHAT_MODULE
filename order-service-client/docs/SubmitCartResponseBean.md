# SubmitCartResponseBean


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **int** |  | [optional] 

## Example

```python
from order_api_client.models.submit_cart_response_bean import SubmitCartResponseBean

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitCartResponseBean from a JSON string
submit_cart_response_bean_instance = SubmitCartResponseBean.from_json(json)
# print the JSON string representation of the object
print(SubmitCartResponseBean.to_json())

# convert the object into a dict
submit_cart_response_bean_dict = submit_cart_response_bean_instance.to_dict()
# create an instance of SubmitCartResponseBean from a dict
submit_cart_response_bean_from_dict = SubmitCartResponseBean.from_dict(submit_cart_response_bean_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


