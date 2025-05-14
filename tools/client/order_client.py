import requests
from typing import List

class OrderClient:

    def __init__(self, base_url: str):
        self.base_url = base_url

    def place_order(self, user_id: str, total_amount: int, details: str) -> dict:
        payload = {
            "userId": user_id,
            "totalAmount": total_amount,
            "details": details,
            "status": "pending"
        }
        response = requests.post(f"{self.base_url}/orders/place", json=payload)
        response.raise_for_status()
        return response.json()

    def get_order_status(self, order_id: str) -> str:
        response = requests.get(f"{self.base_url}/orders/status/{order_id}")
        response.raise_for_status()
        return response.text

    def cancel_order(self, user_id: str) -> str:
        response = requests.post(f"{self.base_url}/orders/cancel/{user_id}")
        response.raise_for_status()
        return response.text

# Example Usage
if __name__ == "__main__":
    client = OrderClient()

    # 1. Place a new order
    order = client.place_order(user_id="user123", total_amount=5000, details="Samsung Galaxy Phone")
    print("Placed Order:", order)

    order_id = order['id']

    # 2. Check status
    status = client.get_order_status(order_id)
    print("Order Status:", status)

    # 3. Pay for order
    payment_response = client.pay_order(order_id)
    print("Payment Response:", payment_response)

    # 4. View all active orders
    active_orders = client.view_active_orders()
    print("Active Orders:", active_orders)

    # 5. Process (deliver) the order
    delivery_response = client.process_order(order_id)
    print("Delivery Response:", delivery_response)

    # 6. Cancel (won't work if already delivered)
    cancel_response = client.cancel_order(user_id="user123")
    print("Cancel Response:", cancel_response)
