import sys
from typing import Optional
from pydantic import BaseModel, Field
from langchain_core.tools import tool

sys.path.append('./product-service-client')

from product_api_client.api.product_api import ProductApi
from product_api_client.models.get_products_request import GetProductsRequest
from product_api_client.models.get_products_request_bean import GetProductsRequestBean
from product_api_client.configuration import Configuration
from product_api_client.api_client import ApiClient

# Pydantic Model for Handling API Responses
# This model is used to represent product data as it is returned by the API
class ProductBean(BaseModel):
    id: str
    name: str
    description: str
    image_path: str
    price: int
    stock: int
    category: str
    brand: str


class GetProductsResponse(BaseModel):
    products: list[ProductBean]

# API Client Configuration
# This part initializes the connection configuration for the API.
configuration = Configuration(
    host="http://localhost:8025/api"  # Specify the API's base URL
)

# Functions to generate requests for fetching product data based on different filters

def create_get_all_products_request(channel: int, deviceId: str, deviceType: str, userId: int, token: Optional[str]) -> GetProductsRequest:
    """
    Generates a request to fetch all products without any filters.
    """
    return GetProductsRequest(
        channel=channel,
        deviceId=deviceId,
        deviceType=deviceType,
        userId=userId,
        token=token,
        productsRequestBean=GetProductsRequestBean()
    )


def create_get_products_by_category_request(channel: int, deviceId: str, deviceType: str, userId: int, token: Optional[str], categoryId: int) -> GetProductsRequest:
    """
    Generates a request to fetch products filtered by category.
    """
    return GetProductsRequest(
        channel=channel,
        deviceId=deviceId,
        deviceType=deviceType,
        userId=userId,
        token=token,
        productsRequestBean=GetProductsRequestBean(categoryId=categoryId)
    )


def create_get_products_by_brand_request(channel: int, deviceId: str, deviceType: str, userId: int, token: Optional[str], brandId: int) -> GetProductsRequest:
    """
    Generates a request to fetch products filtered by brand.
    """
    return GetProductsRequest(
        channel=channel,
        deviceId=deviceId,
        deviceType=deviceType,
        userId=userId,
        token=token,
        productsRequestBean=GetProductsRequestBean(brandId=brandId)
    )


def create_get_products_by_brand_and_category_request(channel: int, deviceId: str, deviceType: str, userId: int, token: Optional[str], categoryId: int, brandId: int) -> GetProductsRequest:
    """
    Generates a request to fetch products filtered by both category and brand.
    """
    return GetProductsRequest(
        channel=channel,
        deviceId=deviceId,
        deviceType=deviceType,
        userId=userId,
        token=token,
        productsRequestBean=GetProductsRequestBean(categoryId=categoryId, brandId=brandId)
    )


def create_get_products_by_brand_and_category_min_price_max_price_request(channel: int, deviceId: str, deviceType: str, userId: int, token: Optional[str], categoryId: int, brandId: int, minPrice: float, maxPrice: float) -> GetProductsRequest:
    """
    Generates a request to fetch products filtered by both category and brand with price constraints.
    """
    return GetProductsRequest(
        channel=channel,
        deviceId=deviceId,
        deviceType=deviceType,
        userId=userId,
        token=token,
        productsRequestBean=GetProductsRequestBean(categoryId=categoryId, brandId=brandId, minPrice=minPrice, maxPrice=maxPrice)
    )


def create_get_products_by_brand_and_category_min_max_price_rating_request(channel: int, deviceId: str, deviceType: str, userId: int, token: Optional[str], categoryId: int, brandId: int, minPrice: float, maxPrice: float, minRating: int) -> GetProductsRequest:
    """
    Generates a request to fetch products filtered by both category and brand with price and rating constraints.
    """
    return GetProductsRequest(
        channel=channel,
        deviceId=deviceId,
        deviceType=deviceType,
        userId=userId,
        token=token,
        productsRequestBean=GetProductsRequestBean(categoryId=categoryId, brandId=brandId, minPrice=minPrice, maxPrice=maxPrice, minRating=minRating)
    )


# Function to execute the API request and handle the response
def get_product_api_response(request: GetProductsRequest) -> list[ProductBean]:
    """
    Executes the API request to fetch product data and converts the response into a list of ProductBean objects.
    """
    with ApiClient(configuration) as api_client:
        api_instance = ProductApi(api_client)
        try:
            response = api_instance.get_products(request)
            products = response.get_products_response_bean.products
            return [ProductBean(**product.model_dump()) for product in products]  # Use model_dump() here
        except Exception as e:
            print(e)
            return str({"error": "Error occurred while fetching products"})

# Helper functions for more specific product fetching based on filters
# These functions are designed to simplify the task of fetching products by different criteria

@tool
def get_all_products(channel: int, deviceId: str, deviceType: str, userId: int, token: Optional[str]) -> list[ProductBean]:
    """
    Fetches all products by calling the relevant API endpoint.
    """
    request = create_get_all_products_request(channel, deviceId, deviceType, userId, token)
    return get_product_api_response(request)


@tool
def get_products_by_category(channel: int, deviceId: str, deviceType: str, userId: int, token: Optional[str], categoryId: int) -> list[ProductBean]:
    """
    Fetches products filtered by category.
    """
    request = create_get_products_by_category_request(channel, deviceId, deviceType, userId, token, categoryId)
    return get_product_api_response(request)


@tool
def get_products_by_brand(channel: int, deviceId: str, deviceType: str, userId: int, token: Optional[str], brandId: int) -> list[ProductBean]:
    """
    Fetches products filtered by brand.
    """
    request = create_get_products_by_brand_request(channel, deviceId, deviceType, userId, token, brandId)
    return get_product_api_response(request)


@tool
def get_products_by_brand_and_category(channel: int, deviceId: str, deviceType: str, userId: int, token: Optional[str], categoryId: int, brandId: int) -> list[ProductBean]:
    """
    Fetches products filtered by both brand and category.
    """
    request = create_get_products_by_brand_and_category_request(channel, deviceId, deviceType, userId, token, categoryId, brandId)
    return get_product_api_response(request)


@tool
def get_products_by_brand_and_category_min_price_max_price(channel: int, deviceId: str, deviceType: str, userId: int, token: Optional[str], categoryId: int, brandId: int, minPrice: float, maxPrice: float) -> list[ProductBean]:
    """
    Fetches products filtered by category, brand, and price range.
    """
    request = create_get_products_by_brand_and_category_min_price_max_price_request(channel, deviceId, deviceType, userId, token, categoryId, brandId, minPrice, maxPrice)
    return get_product_api_response(request)


@tool
def get_products_by_brand_and_category_min_max_price_rating(channel: int, deviceId: str, deviceType: str, userId: int, token: Optional[str], categoryId: int, brandId: int, minPrice: float, maxPrice: float, minRating: int) -> list[ProductBean]:
    """
    Fetches products filtered by category, brand, price range, and minimum rating.
    """
    request = create_get_products_by_brand_and_category_min_max_price_rating_request(channel, deviceId, deviceType, userId, token, categoryId, brandId, minPrice, maxPrice, minRating)
    return get_product_api_response(request)

# Main function to test fetching all products
if __name__ == '__main__':
    print(get_all_products(1, '100', 'WEB', 352, None))
