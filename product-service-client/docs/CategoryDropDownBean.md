# CategoryDropDownBean


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**categories** | [**List[CategoryBean]**](CategoryBean.md) |  | [optional] 

## Example

```python
from product_api_client.models.category_drop_down_bean import CategoryDropDownBean

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryDropDownBean from a JSON string
category_drop_down_bean_instance = CategoryDropDownBean.from_json(json)
# print the JSON string representation of the object
print(CategoryDropDownBean.to_json())

# convert the object into a dict
category_drop_down_bean_dict = category_drop_down_bean_instance.to_dict()
# create an instance of CategoryDropDownBean from a dict
category_drop_down_bean_from_dict = CategoryDropDownBean.from_dict(category_drop_down_bean_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


