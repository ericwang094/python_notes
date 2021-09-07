import unittest
from greet_user import get_stored_username


class NamesTestCase(unittest.TestCase):
    def test_get_stored_username(self):
        formatted_name = get_stored_username()
        self.assertEqual(formatted_name, 'Eric')
