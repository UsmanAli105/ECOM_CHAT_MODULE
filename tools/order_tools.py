from pydantic import BaseModel
from langchain_core.tools import tool
from tools.client.order_client import OrderClient
from tools.util import *

# Schema definitions
class PlaceOrderSchema(BaseModel):
    user_id: str
    total_amount: int
    details: str

class GetOrderStatusSchema(BaseModel):
    order_id: str

class CancelOrderSchema(BaseModel):
    user_id: str

# Constants
BASE_URL = 'http://localhost:8082/api'

# Order client instance
orderClient = OrderClient(BASE_URL)

# Place Order Tool
@tool(
    args_schema=PlaceOrderSchema,
    description="Call this tool to place an order. Gather all items user wants to order and send them as a comma-separated string."
)
def place_order(user_id: str, total_amount: int, details: str):
    try:
        response = orderClient.place_order(
            user_id=user_id,
            total_amount=total_amount,
            details=details,
        )
        return {"success": "Order placed.", "order_id": response.get("id")}
    except Exception as e:
        return {"error": f"Order could not be placed. Reason: {str(e)}"}

# Get Order Status Tool
@tool(
    args_schema=GetOrderStatusSchema,
    description="Call this tool to check the order status. Get the order ID from the user first."
)
def get_order_status(order_id: str):
    try:
        status = orderClient.get_order_status(order_id)
        return {"status": status}
    except Exception as e:
        return {"error": f"Couldn't get order status. Reason: {str(e)}"}

# Cancel Order Tool
@tool(
    args_schema=CancelOrderSchema,
    description="Call this tool to cancel existing order(s) for a user. Get the user ID from the user first."
)
def cancel_order(user_id: str):
    try:
        response = orderClient.cancel_order(user_id)
        return {"success": response}
    except Exception as e:
        return {"error": f"Order could not be canceled. Reason: {str(e)}"}
