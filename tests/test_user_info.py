import unittest
import user_info

class MyTestCase(unittest.TestCase):
    def test_age_prompt(self):
        info = user_info.UserInfo(1)
        info.set_user_birthdate("1990-01-01")
        self.assertEqual(info.populate_age_info(), "They are 34 years old.")
        info = user_info.UserInfo(1)
        info.set_user_birthdate("2023-01-01")
        self.assertEqual(info.populate_age_info(), "They are 1 year old.")

    def test_height_prompt(self):
        info = user_info.UserInfo(1)
        info.set_user_height(180)
        self.assertEqual(info.populate_height_info(), "They are 180 cm tall.")

    def test_weight_prompt(self):
        info = user_info.UserInfo(1)
        info.set_user_weight(80)
        self.assertEqual(info.populate_weight_info(), "They weigh 80 kg.")

    def test_calorie_intake_prompt(self):
        info = user_info.UserInfo(1)
        info.set_user_daily_calorie_intake(2500)
        self.assertEqual(info.populate_calorie_consumption_info(), "On average, this patient consumes 2500 calories per day.")

    def test_calorie_burn_prompt(self):
        info = user_info.UserInfo(1)
        info.set_user_daily_calorie_burn(2000)
        self.assertEqual(info.populate_calorie_burn_info(), "On average, this patient burns 2000 calories per day.")

    def test_user_question_prompt(self):
        user_question = "What should I eat?"
        info = user_info.UserInfo(1)
        info.add_user_question(user_question)
        self.assertEqual(info.populate_user_questions(), "The user has the following question:\nWhat should I eat?")

if __name__ == '__main__':
    unittest.main()
