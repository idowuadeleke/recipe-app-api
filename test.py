from django.test import TestCase

from app.calc import add


class CalcTests(TestCase):

    def test_add_numbers(self):
        """Test add two numbers together"""
        self.assertEqual(add(2, 3), 5)