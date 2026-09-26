def summarize_orders(orders):
    """
    Summarize order statistics.

    Order shape:
    {
        "id": 1,
        "status": "completed",
        "total": 100.50,
    }
    """
    total_revenue = 0
    completed_orders = 0
    cancelled_orders = 0

    for order in orders:
        if order["status"] == "completed":
            completed_orders += 1
            total_revenue += order["total"]

        if order["status"] == "cancelled":
            cancelled_orders += 1

    average_order_value = total_revenue / completed_orders

    return {
        "total_orders": completed_orders,
        "completed_orders": completed_orders,
        "cancelled_orders": cancelled_orders,
        "total_revenue": round(total_revenue, 2),
        "average_order_value": round(average_order_value, 2),
    }
