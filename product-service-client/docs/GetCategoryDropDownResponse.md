# GetCategoryDropDownResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**Status**](Status.md) |  | [optional] 
**data** | [**CategoryDropDownBean**](CategoryDropDownBean.md) |  | [optional] 

## Example

```python
from product_api_client.models.get_category_drop_down_response import GetCategoryDropDownResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCategoryDropDownResponse from a JSON string
get_category_drop_down_response_instance = GetCategoryDropDownResponse.from_json(json)
# print the JSON string representation of the object
print(GetCategoryDropDownResponse.to_json())

# convert the object into a dict
get_category_drop_down_response_dict = get_category_drop_down_response_instance.to_dict()
# create an instance of GetCategoryDropDownResponse from a dict
get_category_drop_down_response_from_dict = GetCategoryDropDownResponse.from_dict(get_category_drop_down_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


