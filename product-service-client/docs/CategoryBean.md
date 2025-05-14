# CategoryBean


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from product_api_client.models.category_bean import CategoryBean

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryBean from a JSON string
category_bean_instance = CategoryBean.from_json(json)
# print the JSON string representation of the object
print(CategoryBean.to_json())

# convert the object into a dict
category_bean_dict = category_bean_instance.to_dict()
# create an instance of CategoryBean from a dict
category_bean_from_dict = CategoryBean.from_dict(category_bean_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


