# ProductCountBean


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from product_api_client.models.product_count_bean import ProductCountBean

# TODO update the JSON string below
json = "{}"
# create an instance of ProductCountBean from a JSON string
product_count_bean_instance = ProductCountBean.from_json(json)
# print the JSON string representation of the object
print(ProductCountBean.to_json())

# convert the object into a dict
product_count_bean_dict = product_count_bean_instance.to_dict()
# create an instance of ProductCountBean from a dict
product_count_bean_from_dict = ProductCountBean.from_dict(product_count_bean_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


