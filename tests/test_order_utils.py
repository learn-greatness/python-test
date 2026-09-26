import unittest
from src.order_utils import calculate_order_total


class TestOrderTotal(unittest.TestCase):
    def test_basic_total(self):
        order = {
            "items": [
                {"price": 100, "quantity": 2},
                {"price": 50, "quantity": 1},
            ],
            "discount_percent": 10,
            "tax_percent": 18,
        }

        self.assertEqual(calculate_order_total(order), 212.40)

    def test_does_not_mutate_input(self):
        order = {
            "items": [{"price": 100, "quantity": 2}],
            "discount_percent": 0,
            "tax_percent": 0,
        }

        original_quantity = order["items"][0]["quantity"]
        calculate_order_total(order)

        self.assertEqual(order["items"][0]["quantity"], original_quantity)


if __name__ == "__main__":
    unittest.main()
