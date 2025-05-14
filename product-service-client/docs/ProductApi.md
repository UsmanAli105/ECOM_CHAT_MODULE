# product_api_client.ProductApi

All URIs are relative to *http://localhost:8025/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_product**](ProductApi.md#create_product) | **POST** /product/create | 
[**get_product_count**](ProductApi.md#get_product_count) | **POST** /product/count | 
[**get_products**](ProductApi.md#get_products) | **POST** /product/get | 


# **create_product**
> CreateProductResponse create_product(create_products_request)

### Example


```python
import product_api_client
from product_api_client.models.create_product_response import CreateProductResponse
from product_api_client.models.create_products_request import CreateProductsRequest
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
    api_instance = product_api_client.ProductApi(api_client)
    create_products_request = product_api_client.CreateProductsRequest() # CreateProductsRequest | 

    try:
        api_response = api_instance.create_product(create_products_request)
        print("The response of ProductApi->create_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->create_product: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_products_request** | [**CreateProductsRequest**](CreateProductsRequest.md)|  | 

### Return type

[**CreateProductResponse**](CreateProductResponse.md)

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

# **get_product_count**
> GetProductCountResponse get_product_count(get_product_count_request)

### Example


```python
import product_api_client
from product_api_client.models.get_product_count_request import GetProductCountRequest
from product_api_client.models.get_product_count_response import GetProductCountResponse
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
    api_instance = product_api_client.ProductApi(api_client)
    get_product_count_request = product_api_client.GetProductCountRequest() # GetProductCountRequest | 

    try:
        api_response = api_instance.get_product_count(get_product_count_request)
        print("The response of ProductApi->get_product_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->get_product_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_product_count_request** | [**GetProductCountRequest**](GetProductCountRequest.md)|  | 

### Return type

[**GetProductCountResponse**](GetProductCountResponse.md)

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

# **get_products**
> GetProductsResponse get_products(get_products_request)

### Example


```python
import product_api_client
from product_api_client.models.get_products_request import GetProductsRequest
from product_api_client.models.get_products_response import GetProductsResponse
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
    api_instance = product_api_client.ProductApi(api_client)
    get_products_request = product_api_client.GetProductsRequest() # GetProductsRequest | 

    try:
        api_response = api_instance.get_products(get_products_request)
        print("The response of ProductApi->get_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->get_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_products_request** | [**GetProductsRequest**](GetProductsRequest.md)|  | 

### Return type

[**GetProductsResponse**](GetProductsResponse.md)

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

