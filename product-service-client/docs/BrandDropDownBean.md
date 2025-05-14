# BrandDropDownBean


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**brands** | [**List[BrandBean]**](BrandBean.md) |  | [optional] 

## Example

```python
from product_api_client.models.brand_drop_down_bean import BrandDropDownBean

# TODO update the JSON string below
json = "{}"
# create an instance of BrandDropDownBean from a JSON string
brand_drop_down_bean_instance = BrandDropDownBean.from_json(json)
# print the JSON string representation of the object
print(BrandDropDownBean.to_json())

# convert the object into a dict
brand_drop_down_bean_dict = brand_drop_down_bean_instance.to_dict()
# create an instance of BrandDropDownBean from a dict
brand_drop_down_bean_from_dict = BrandDropDownBean.from_dict(brand_drop_down_bean_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


