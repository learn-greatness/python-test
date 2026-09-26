import unittest
from src.analytics import summarize_orders


class TestAnalytics(unittest.TestCase):
    def test_summary(self):
        orders = [
            {"id": 1, "status": "completed", "total": 100},
            {"id": 2, "status": "completed", "total": 50.50},
            {"id": 3, "status": "cancelled", "total": 999},
            {"id": 4, "status": "pending", "total": 200},
        ]

        self.assertEqual(
            summarize_orders(orders),
            {
                "total_orders": 4,
                "completed_orders": 2,
                "cancelled_orders": 1,
                "total_revenue": 150.50,
                "average_order_value": 75.25,
            },
        )


if __name__ == "__main__":
    unittest.main()
