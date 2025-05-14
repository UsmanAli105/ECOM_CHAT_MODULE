# order_api_client.CartApi

All URIs are relative to *http://localhost:8030/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_to_cart**](CartApi.md#add_to_cart) | **POST** /cart/add | 
[**delete_from_cart**](CartApi.md#delete_from_cart) | **POST** /cart/delete | 
[**submit_cart**](CartApi.md#submit_cart) | **POST** /cart/submit | 
[**view_cart**](CartApi.md#view_cart) | **POST** /cart/view | 


# **add_to_cart**
> AddToCartResponse add_to_cart(add_to_cart_request)

### Example


```python
import order_api_client
from order_api_client.models.add_to_cart_request import AddToCartRequest
from order_api_client.models.add_to_cart_response import AddToCartResponse
from order_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8030/api
# See configuration.py for a list of all supported configuration parameters.
configuration = order_api_client.Configuration(
    host = "http://localhost:8030/api"
)


# Enter a context with an instance of the API client
with order_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = order_api_client.CartApi(api_client)
    add_to_cart_request = order_api_client.AddToCartRequest() # AddToCartRequest | 

    try:
        api_response = api_instance.add_to_cart(add_to_cart_request)
        print("The response of CartApi->add_to_cart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartApi->add_to_cart: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_to_cart_request** | [**AddToCartRequest**](AddToCartRequest.md)|  | 

### Return type

[**AddToCartResponse**](AddToCartResponse.md)

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

# **delete_from_cart**
> DeleteFromCartResponse delete_from_cart(delete_from_cart_request)

### Example


```python
import order_api_client
from order_api_client.models.delete_from_cart_request import DeleteFromCartRequest
from order_api_client.models.delete_from_cart_response import DeleteFromCartResponse
from order_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8030/api
# See configuration.py for a list of all supported configuration parameters.
configuration = order_api_client.Configuration(
    host = "http://localhost:8030/api"
)


# Enter a context with an instance of the API client
with order_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = order_api_client.CartApi(api_client)
    delete_from_cart_request = order_api_client.DeleteFromCartRequest() # DeleteFromCartRequest | 

    try:
        api_response = api_instance.delete_from_cart(delete_from_cart_request)
        print("The response of CartApi->delete_from_cart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartApi->delete_from_cart: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_from_cart_request** | [**DeleteFromCartRequest**](DeleteFromCartRequest.md)|  | 

### Return type

[**DeleteFromCartResponse**](DeleteFromCartResponse.md)

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

# **submit_cart**
> SubmitCartResponse submit_cart(submit_cart_request)

### Example


```python
import order_api_client
from order_api_client.models.submit_cart_request import SubmitCartRequest
from order_api_client.models.submit_cart_response import SubmitCartResponse
from order_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8030/api
# See configuration.py for a list of all supported configuration parameters.
configuration = order_api_client.Configuration(
    host = "http://localhost:8030/api"
)


# Enter a context with an instance of the API client
with order_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = order_api_client.CartApi(api_client)
    submit_cart_request = order_api_client.SubmitCartRequest() # SubmitCartRequest | 

    try:
        api_response = api_instance.submit_cart(submit_cart_request)
        print("The response of CartApi->submit_cart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartApi->submit_cart: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submit_cart_request** | [**SubmitCartRequest**](SubmitCartRequest.md)|  | 

### Return type

[**SubmitCartResponse**](SubmitCartResponse.md)

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

# **view_cart**
> ViewCartResponse view_cart(view_cart_request)

### Example


```python
import order_api_client
from order_api_client.models.view_cart_request import ViewCartRequest
from order_api_client.models.view_cart_response import ViewCartResponse
from order_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8030/api
# See configuration.py for a list of all supported configuration parameters.
configuration = order_api_client.Configuration(
    host = "http://localhost:8030/api"
)


# Enter a context with an instance of the API client
with order_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = order_api_client.CartApi(api_client)
    view_cart_request = order_api_client.ViewCartRequest() # ViewCartRequest | 

    try:
        api_response = api_instance.view_cart(view_cart_request)
        print("The response of CartApi->view_cart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartApi->view_cart: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_cart_request** | [**ViewCartRequest**](ViewCartRequest.md)|  | 

### Return type

[**ViewCartResponse**](ViewCartResponse.md)

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

