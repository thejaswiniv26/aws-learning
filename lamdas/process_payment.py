import json

def lambda_handler(event, context):
    """
    Process payment if order is valid.
    """
    order_id = event.get("orderId")
    valid = event.get("valid", False)

    if not valid:
        return {
            "orderId": order_id,
            "payment": "failed",
            "message": "Invalid order"
        }

    # For demo, we assume payment always succeeds
    return {
        "orderId": order_id,
        "payment": "success",
        "message": "Payment processed successfully"
    }
