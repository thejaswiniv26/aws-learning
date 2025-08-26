import json

def lambda_handler(event, context):
    """
    Validate if the order has items.
    """
    order_id = event.get("orderId")
    items = event.get("items", [])

    if not items:
        return {
            "orderId": order_id,
            "valid": False,
            "message": "Order has no items"
        }

    return {
        "orderId": order_id,
        "valid": True,
        "message": "Order validated successfully"
    }
