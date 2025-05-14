import sys
from typing import Optional
from pydantic import BaseModel, Field
from langchain_core.tools import tool

import sys
print(sys.path)
sys.path.append('H:/Data/MSDS/Semester_4/Operating_Systems/Semester_Project/ChatApp/order-service-client')

from order_api_client.api.cart_api import CartApi
from order_api_client.api.cart_api import CartApi
from order_api_client.models.add_to_cart_request import AddToCartRequest
from order_api_client.models.add_to_cart_request_bean import AddToCartRequestBean
from order_api_client.models.add_to_cart_response import AddToCartResponse

from order_api_client.models.view_cart_request import ViewCartRequest
from order_api_client.models.view_cart_response import ViewCartResponse

def create_add_to_cart_request(channel, device_id, device_type, user_id, token, product_id, quantity, unit_price):
    return AddToCartRequest(
        channel=channel,
        device_id=device_id,
        device_type=device_type,
        user_id=user_id,
        token=token,
        add_to_cart_request_bean=AddToCartRequestBean(
            product_id=product_id,
            quantity=quantity,
            unit_price=unit_price
        )
    )


def create_view_cart_request(channel, device_id, device_type, user_id, token):
    return ViewCartRequest(
        channel=channel,
        device_id=device_id,
        device_type=device_type,
        user_id=user_id,
        token=token,
    )

@tool
def add_item_to_cart(channel: int, device_id: str, device_type: str, user_id: int, token: Optional[str], product_id: str, quantity: int, unit_price: float):
    """Call this  function to add an item to cart"""
    request = create_add_to_cart_request(channel, device_id, device_type, user_id, token, product_id, quantity, unit_price)
    cart_api = CartApi()
    try:
        response = cart_api.add_to_cart(request)
        if isinstance(response, AddToCartResponse):
            if response.add_to_cart_response_bean.success == True:
                return(f"Item added to cart successfully! Cart size: {response.add_to_cart_response_bean.current_cart_size}")
            else:
                return(f"Couldn't add item to cart. Reason: {response.status.message}")
        else:
            return "Failed to add item to cart."
    except Exception as e:
        return f"An error occurred while adding item to cart: {e}"



@tool
def view_cart(channel: int, device_id: str, device_type: str, user_id: int, token: Optional[str]):
    """Call this  function to view added items to cart"""
    request = create_view_cart_request(channel, device_id, device_type, user_id, token)
    cart_api = CartApi()
    try:
        response = cart_api.view_cart(request)
        if isinstance(response, ViewCartResponse):
            print(response)
            if response.view_cart_bean is not None:
                return response.view_cart_bean
            else:
                return(f"Couldn't fetch items from cart. Reason: {response.status.message}")
        else:
            return "Failed to fetch items from cart."
    except Exception as e:
        return f"An error occurred while fetching items from cart: {e}"


# if __name__ == '__main__':
#     res = add_item_to_cart.invoke({
#         "channel": 1,
#         "device_id": "123",
#         "device_type": "WEB",
#         "user_id": 123,
#         "token": None,
#         "product_id": "12a98add-154e-4b3a-8cb6-df33826c9d01",
#         "quantity": 1,
#         "unit_price": 222310
#     })
#     print(res)
