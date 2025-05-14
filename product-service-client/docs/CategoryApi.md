# product_api_client.CategoryApi

All URIs are relative to *http://localhost:8025/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_category_drop_down**](CategoryApi.md#get_category_drop_down) | **POST** /category/getDropDown | 


# **get_category_drop_down**
> GetCategoryDropDownResponse get_category_drop_down(get_category_drop_down_request)

### Example


```python
import product_api_client
from product_api_client.models.get_category_drop_down_request import GetCategoryDropDownRequest
from product_api_client.models.get_category_drop_down_response import GetCategoryDropDownResponse
from product_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8025/api
# See configuration.py for a list of all supported configuration parameters.
configuration = product_api_client.Configuration(
    host = "http://localhost:8025/api"
)


# Enter a context with an instance of the API client
with product_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = product_api_client.CategoryApi(api_client)
    get_category_drop_down_request = product_api_client.GetCategoryDropDownRequest() # GetCategoryDropDownRequest | 

    try:
        api_response = api_instance.get_category_drop_down(get_category_drop_down_request)
        print("The response of CategoryApi->get_category_drop_down:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoryApi->get_category_drop_down: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_category_drop_down_request** | [**GetCategoryDropDownRequest**](GetCategoryDropDownRequest.md)|  | 

### Return type

[**GetCategoryDropDownResponse**](GetCategoryDropDownResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

