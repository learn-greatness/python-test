class OrderNotFoundError(Exception):
    pass


class InvalidOrderStateError(Exception):
    pass


class OrderService:
    def __init__(self):
        self.orders = {}
        self.next_id = 1

    def create_order(self, user_id, items): 
        """
        Create and store a pending order.

        Each item should look like:
        {"product_id": 123, "quantity": 2}
        """
        if user_id <= 0:
            raise ValueError("user_id must be positive")

        if not items:
            raise ValueError("order must contain at least one item")

        order = {
            "id": self.next_id,
            "user_id": user_id,
            "items": items,
            "status": "pending",
        }

        self.orders[self.next_id] = order
        self.next_id += 1

        return order
    
    def get_order(self, order_id):
        if order_id not in self.orders:
            raise OrderNotFoundError("Order not found")


        return self.orders[order_id]

    
    def cancel_order(self, order_id):
        if order_id not in self.orders:
            raise OrderNotFoundError("Order not found")

        order = self.orders[order_id]

        if order["status"] != "pending":
            raise InvalidOrderStateError("Only pending orders can be cancelled")

        order["status"] = "cancelled"

        return order
