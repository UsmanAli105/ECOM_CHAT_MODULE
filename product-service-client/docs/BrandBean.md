# BrandBean


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from product_api_client.models.brand_bean import BrandBean

# TODO update the JSON string below
json = "{}"
# create an instance of BrandBean from a JSON string
brand_bean_instance = BrandBean.from_json(json)
# print the JSON string representation of the object
print(BrandBean.to_json())

# convert the object into a dict
brand_bean_dict = brand_bean_instance.to_dict()
# create an instance of BrandBean from a dict
brand_bean_from_dict = BrandBean.from_dict(brand_bean_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


