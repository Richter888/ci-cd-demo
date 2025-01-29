import unittest
from app import hello_world  # Zakładając, że masz funkcję hello_world w app.py

class TestApp(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello, CI/CD!")

if __name__ == '__main__':
    unittest.main()
