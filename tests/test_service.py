import unittest
from src.service import OrderService


class TestOrderService(unittest.TestCase):
    def test_create_order(self):
        service = OrderService()

        order = service.create_order(
            1,
            [{"product_id": 10, "quantity": 2}],
        )

        self.assertEqual(order["id"], 1)
        self.assertEqual(order["status"], "pending")

    def test_get_existing_order(self):
        service = OrderService()
        created = service.create_order(
            1,
            [{"product_id": 10, "quantity": 2}],
        )

        self.assertEqual(service.get_order(created["id"]), created)


if __name__ == "__main__":
    unittest.main()
