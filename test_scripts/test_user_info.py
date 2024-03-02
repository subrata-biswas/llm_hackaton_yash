import unittest
import user_info

class MyTestCase(unittest.TestCase):
    def test_age(self):
        info = user_info.UserInfo(1)
        info.set_user_birthdate("1990-01-01")
        self.assertEqual(info.populate_user_info(), "We have a 34 years old patient")
        info = user_info.UserInfo(1)
        info.set_user_birthdate("2023-01-01")
        self.assertEqual(info.populate_user_info(), "We have a 1 year old patient")


if __name__ == '__main__':
    unittest.main()
