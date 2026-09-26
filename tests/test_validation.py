import unittest
from src.validation import validate_user


class TestValidation(unittest.TestCase):
    def test_valid_user(self):
        self.assertTrue(
            validate_user({
                "name": "Alice",
                "email": "alice@example.com",
                "age": 22,
            })
        )

    def test_invalid_email(self):
        self.assertFalse(
            validate_user({
                "name": "Alice",
                "email": "alice.example.com",
                "age": 22,
            })
        )


if __name__ == "__main__":
    unittest.main()
