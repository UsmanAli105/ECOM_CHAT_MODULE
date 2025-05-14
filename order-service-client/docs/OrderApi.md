# order_api_client.OrderApi

All URIs are relative to *http://localhost:8030/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_new_orders**](OrderApi.md#get_new_orders) | **POST** /order/getNewOrders | 
[**get_order_count**](OrderApi.md#get_order_count) | **POST** /order/getOrdersCount | 
[**update_order_status**](OrderApi.md#update_order_status) | **POST** /order/updateOrderStatus | 


# **get_new_orders**
> GetNewOrdersResponse get_new_orders(get_new_orders_request)

### Example


```python
import order_api_client
from order_api_client.models.get_new_orders_request import GetNewOrdersRequest
from order_api_client.models.get_new_orders_response import GetNewOrdersResponse
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
    api_instance = order_api_client.OrderApi(api_client)
    get_new_orders_request = order_api_client.GetNewOrdersRequest() # GetNewOrdersRequest | 

    try:
        api_response = api_instance.get_new_orders(get_new_orders_request)
        print("The response of OrderApi->get_new_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->get_new_orders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_new_orders_request** | [**GetNewOrdersRequest**](GetNewOrdersRequest.md)|  | 

### Return type

[**GetNewOrdersResponse**](GetNewOrdersResponse.md)

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

# **get_order_count**
> GetOrderCountResponse get_order_count(get_order_count_request)

### Example


```python
import order_api_client
from order_api_client.models.get_order_count_request import GetOrderCountRequest
from order_api_client.models.get_order_count_response import GetOrderCountResponse
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
    api_instance = order_api_client.OrderApi(api_client)
    get_order_count_request = order_api_client.GetOrderCountRequest() # GetOrderCountRequest | 

    try:
        api_response = api_instance.get_order_count(get_order_count_request)
        print("The response of OrderApi->get_order_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->get_order_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_order_count_request** | [**GetOrderCountRequest**](GetOrderCountRequest.md)|  | 

### Return type

[**GetOrderCountResponse**](GetOrderCountResponse.md)

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

# **update_order_status**
> UpdateOrderStatusResponse update_order_status(update_order_status_request)

### Example


```python
import order_api_client
from order_api_client.models.update_order_status_request import UpdateOrderStatusRequest
from order_api_client.models.update_order_status_response import UpdateOrderStatusResponse
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
    api_instance = order_api_client.OrderApi(api_client)
    update_order_status_request = order_api_client.UpdateOrderStatusRequest() # UpdateOrderStatusRequest | 

    try:
        api_response = api_instance.update_order_status(update_order_status_request)
        print("The response of OrderApi->update_order_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->update_order_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_order_status_request** | [**UpdateOrderStatusRequest**](UpdateOrderStatusRequest.md)|  | 

### Return type

[**UpdateOrderStatusResponse**](UpdateOrderStatusResponse.md)

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

