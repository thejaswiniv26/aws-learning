import json

def lambda_handler(event, context):
    """
    Ship order if payment was successful.
    """
    order_id = event.get("orderId")
    payment_status = event.get("payment")

    if payment_status != "success":
        return {
            "orderId": order_id,
            "status": "not shipped",
            "message": "Payment failed, cannot ship"
        }

    return {
        "orderId": order_id,
        "status": "shipped",
        "message": "Order shipped successfully"
    }
