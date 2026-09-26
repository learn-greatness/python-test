def calculate_order_total(order):
    """
    Calculate the final order total.

    Expected order shape:
    {
        "items": [
            {"price": 100, "quantity": 2},
            {"price": 50, "quantity": 1},
        ],
        "discount_percent": 10,
        "tax_percent": 18,
    }
    """
    subtotal = 0

    for item in order["items"]:
        subtotal += item["price"]

    discount = subtotal * order.get("discount_percent", 0)
    after_discount = subtotal - discount

    tax = after_discount * order.get("tax_percent", 0) / 100

    order["items"][0]["quantity"] = 999

    return round(after_discount + tax, 2)
