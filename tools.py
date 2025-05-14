import os
import sys
from pydantic import BaseModel
sys.path.append(r'services')



from services.user_service.api.session_api import SessionApi
from services.user_service.models import *

from services.product_service.api.brand_api import BrandApi
from services.product_service.api.category_api import CategoryApi
from services.product_service.api.product_api import ProductApi
from services.product_service.models import *


from services.order_service.api.cart_api import CartApi
from services.order_service.api.order_api import OrderApi
from services.order_service.models import *

from dotenv import load_dotenv
from constants import *
from typing import Optional
from langchain_core.tools import tool
from session import load_sessions, save_sessions


load_dotenv(override=True)


USER_SERVICE_API_URL = os.getenv("USER_SERVICE_API_URL", "")
PRODUCT_SERVICE_API_URL = os.getenv("PRODUCT_SERVICE_API_URL", "")
ORDER_SERVICE_API_URL = os.getenv("ORDER_SERVICE_API_URL", "")


def check_session(user_id: int, token: str):
    sessionApi = SessionApi(api_client=None)
    sessionApi.api_client.configuration.host = USER_SERVICE_API_URL

    request = CheckSessionRequest(
    channel=DEFAULT_CHANNEL,
    deviceId=DEFAULT_DEVICE_ID,
    deviceType=DEFAULT_DEVICE_TYPE,

    userId=user_id,
    token=token,
    checkSessionRequestBean=CheckSessionRequestBean(
        token=token
        )
    )
    try:
        return sessionApi.check_session(request)
    except Exception as e:
        return f"Error occurred while calling the API: {e}"

@tool(description="Retrieves the list of available product brands for the user. Requires user ID and token for authentication.")
def get_brands(user_id: int, token: str):
    brandApi = BrandApi(api_client=None)
    brandApi.api_client.configuration.host = PRODUCT_SERVICE_API_URL

    request = GetBrandDropDownRequest(
        channel=DEFAULT_CHANNEL,
        deviceId=DEFAULT_DEVICE_ID,
        deviceType=DEFAULT_DEVICE_TYPE,
        userId=user_id,
        token=token
    )

    try:
        return brandApi.get_brand_drop_down(request)
    except Exception as e:
        return f"Error occurred while calling the API: {e}"


@tool(description="Retrieves the list of available product categories for the user. Requires user ID and token for authentication.")
def get_category(user_id: int, token: str):
    categoryApi = CategoryApi(api_client=None)
    categoryApi.api_client.configuration.host = PRODUCT_SERVICE_API_URL

    request = GetCategoryDropDownRequest(
        channel=DEFAULT_CHANNEL,
        deviceId=DEFAULT_DEVICE_ID,
        deviceType=DEFAULT_DEVICE_TYPE,
        userId=user_id,
        token=token
    )

    try:
        return categoryApi.get_category_drop_down(request)
    except Exception as e:
        return f"Error occurred while calling the API: {e}"


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
    productApi = ProductApi(api_client=None)
    productApi.api_client.configuration.host = PRODUCT_SERVICE_API_URL
    try:
        return productApi.get_products(request)
    except Exception as e:
        return f"Error occurred while calling the API: {e}"

@tool
def get_all_products(userId: int, token: Optional[str]) -> list[ProductBean]:
    """
    Fetches all products by calling the relevant API endpoint.
    """
    channel=DEFAULT_CHANNEL
    deviceId=DEFAULT_DEVICE_ID
    deviceType=DEFAULT_DEVICE_TYPE

    request = create_get_all_products_request(channel, deviceId, deviceType, userId, token)
    return get_product_api_response(request)


@tool
def get_products_by_category(userId: int, token: Optional[str], categoryId: int) -> list[ProductBean]:
    """
    Fetches products filtered by category.
    """
    channel=DEFAULT_CHANNEL
    deviceId=DEFAULT_DEVICE_ID
    deviceType=DEFAULT_DEVICE_TYPE


    request = create_get_products_by_category_request(channel, deviceId, deviceType, userId, token, categoryId)
    return get_product_api_response(request)


@tool
def get_products_by_brand(userId: int, token: Optional[str], brandId: int) -> list[ProductBean]:
    """
    Fetches products filtered by brand.
    """
    channel=DEFAULT_CHANNEL
    deviceId=DEFAULT_DEVICE_ID
    deviceType=DEFAULT_DEVICE_TYPE


    request = create_get_products_by_brand_request(channel, deviceId, deviceType, userId, token, brandId)
    return get_product_api_response(request)


@tool
def get_products_by_brand_and_category(userId: int, token: Optional[str], categoryId: int, brandId: int) -> list[ProductBean]:
    """
    Fetches products filtered by both brand and category.
    """
    channel=DEFAULT_CHANNEL
    deviceId=DEFAULT_DEVICE_ID
    deviceType=DEFAULT_DEVICE_TYPE


    request = create_get_products_by_brand_and_category_request(channel, deviceId, deviceType, userId, token, categoryId, brandId)
    return get_product_api_response(request)


@tool
def get_products_by_brand_and_category_min_price_max_price(userId: int, token: Optional[str], categoryId: int, brandId: int, minPrice: float, maxPrice: float) -> list[ProductBean]:
    """
    Fetches products filtered by category, brand, and price range.
    """
    channel=DEFAULT_CHANNEL
    deviceId=DEFAULT_DEVICE_ID
    deviceType=DEFAULT_DEVICE_TYPE


    request = create_get_products_by_brand_and_category_min_price_max_price_request(channel, deviceId, deviceType, userId, token, categoryId, brandId, minPrice, maxPrice)
    return get_product_api_response(request)


@tool
def get_products_by_brand_and_category_min_max_price_rating(userId: int, token: Optional[str], categoryId: int, brandId: int, minPrice: float, maxPrice: float, minRating: int) -> list[ProductBean]:
    """
    Fetches products filtered by category, brand, price range, and minimum rating.
    """
    channel=DEFAULT_CHANNEL
    deviceId=DEFAULT_DEVICE_ID
    deviceType=DEFAULT_DEVICE_TYPE


    request = create_get_products_by_brand_and_category_min_max_price_rating_request(channel, deviceId, deviceType, userId, token, categoryId, brandId, minPrice, maxPrice, minRating)
    return get_product_api_response(request)


@tool(description="Adds a product to the user's shopping cart using the product ID, quantity, and unit price. Requires user ID and token for authentication.")
def add_to_cart(user_id: int, token: str, product_id: str, quantity: int, unit_price: float):
    cartApi = CartApi(api_client=None)
    cartApi.api_client.configuration.host = ORDER_SERVICE_API_URL

    request = AddToCartRequest(
    channel=DEFAULT_CHANNEL,
    deviceId=DEFAULT_DEVICE_ID,
    deviceType=DEFAULT_DEVICE_TYPE,

    userId=user_id,
    token=token,
    addToCartRequestBean=AddToCartRequestBean(
        product_id=product_id,
        quantity=quantity,
        unit_price=unit_price
        )
    )

    try:
        return cartApi.add_to_cart(request)
    except Exception as e:
        return f"Error occurred while calling the API: {e}"

@tool(description="Fetches and returns the current contents of the user's shopping cart. Requires user ID and token for authentication.")
def view_my_cart(user_id: int, token: str):
    cartApi = CartApi(api_client=None)
    cartApi.api_client.configuration.host = ORDER_SERVICE_API_URL

    request = ViewCartRequest(
        channel=DEFAULT_CHANNEL,
        deviceId=DEFAULT_DEVICE_ID,
        deviceType=DEFAULT_DEVICE_TYPE,
        userId=user_id,
        token=token
    )

    try:
        return cartApi.view_cart(request)
    except Exception as e:
        return f"Error occurred while calling the API: {e}"



@tool(description="Submits the user's cart with delivery address and payment info (e.g., Cash on Delivery).")
def submit_cart(
    user_id: int,
    token: str,
    cash_on_delivery: bool,
    agree_terms: bool,
    house: str,
    street: str,
    city: str,
    state: str,
    zip: str,
    country: str,
    phone: str,
    email: str,
    submit: bool = True
):
    """
    Submits a user's cart with all the required information like delivery address,
    payment method, and user authentication details.
    """
    cartApi = CartApi(api_client=None)
    cartApi.api_client.configuration.host = ORDER_SERVICE_API_URL

    request = SubmitCartRequest(
        channel=DEFAULT_CHANNEL,
        deviceId=DEFAULT_DEVICE_ID,
        deviceType=DEFAULT_DEVICE_TYPE,
        userId=user_id,
        token=token,
        submitCartRequestBean=SubmitCartRequestBean(
            cash_on_delivery=cash_on_delivery,
            agree_terms=agree_terms,
            address=UserAddressBean(
                house=house,
                street=street,
                city=city,
                state=state,
                zip=zip,
                country=country,
                phone=phone,
                email=email
            ),
            submit=submit
        )
    )

    try:
        return cartApi.submit_cart(request)
    except Exception as e:
        return f"Error occurred while submitting the cart: {e}"



@tool(description="Check the status of an order by providing the order ID and user credentials.")
def check_order_status(user_id: int, token: str, order_id: int):
    """
    Calls the checkOrderStatus endpoint to retrieve the current status of a specific order.
    """

    orderApi = OrderApi(api_client=None)
    orderApi.api_client.configuration.host = ORDER_SERVICE_API_URL  # Set this constant appropriately

    request = CheckOrderStatusRequest(
        channel=DEFAULT_CHANNEL,
        deviceId=DEFAULT_DEVICE_ID,
        deviceType=DEFAULT_DEVICE_TYPE,
        userId=user_id,
        token=token,
        data=CheckOrderStatusRequestBean(order_id=order_id)
    )

    try:
        return orderApi.check_order_status(request)
    except Exception as e:
        return f"Error occurred while checking order status: {e}"




def is_session_valid(response: CheckSessionResponse) -> bool:
    """
    Evaluates whether the session is valid based on the CheckSessionResponse object.

    Args:
        response (CheckSessionResponse): The response object from check_session.

    Returns:
        bool: True if session is valid, False otherwise.
    """
    print(response)
    # Check if status code exists and equals 200
    if response.status and getattr(response.status, "code", None) == 10000:
        # Optional: If a sessionValid flag exists in the bean, check it
        bean = response.check_session_response_bean
        if bean and hasattr(bean, "session_valid"):
            return getattr(bean, "session_valid", False)
        return True  # status is 200 and bean exists — assume valid
    return False


class UserIdAndToken(BaseModel):
    user_id: int
    token: str


@tool(description="get user _id and token from here")
def get_userid_and_token():
    data = load_sessions()  
    obj = UserIdAndToken(**data)
    return obj


all_tools = [get_brands, get_category, get_all_products, get_products_by_category, get_products_by_brand, get_products_by_brand_and_category, get_products_by_brand_and_category_min_price_max_price, get_products_by_brand_and_category_min_max_price_rating, add_to_cart, view_my_cart, submit_cart, check_order_status, get_userid_and_token]