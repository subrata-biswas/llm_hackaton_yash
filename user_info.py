from datetime import datetime

class UserInfo:
    def __init__(self, user_id):
        self.user_id = user_id

    def get_user_id(self):
        return self.user_id

    def set_user_name(self, name):
        self.name = name

    def get_user_name(self):
        return self.name

    def set_user_birthdate(self, birthdate):
        self.birthdate = birthdate

    def get_user_birthdate(self):
        return self.birthdate

    def set_user_height(self, height):
        self.height = height

    def get_user_height(self):
        return self.height

    def set_user_weight(self, weight):
        self.weight = weight

    def get_user_weight(self):
        return self.weight

    def set_user_daily_calorie_intake(self, calorie_intake):
        self.calorie_intake = calorie_intake

    def get_user_daily_calorie_intake(self):
        return self.calorie_intake

    def set_user_daily_calorie_burn(self, calorie_burn):
        self.calorie_burn = calorie_burn

    def get_user_daily_calorie_burn(self):
        return self.calorie_burn

    def populate_age_info(self):
        age = self.calculate_age(self.get_user_birthdate())
        return (f"They are {age} {self.year_or_years(age)} old.")

    def populate_height_info(self):
        return f"They are {self.get_user_height()} cm tall."

    def populate_weight_info(self):
        return f"They weigh {self.get_user_weight()} kg."

    def populate_calorie_consumption_info(self):
        return (f"On average, this patient consumes {self.get_user_daily_calorie_intake()} calories per day.")

    def populate_calorie_burn_info(self):
        return (f"On average, this patient burns {self.get_user_daily_calorie_burn()} calories per day.")

    def populate_user_info(self):
        age = self.calculate_age(self.get_user_birthdate())
        return "There is a patient." + " " + self.populate_age_info() + " " + self.populate_height_info() + " " + self.populate_weight_info() + " " + self.populate_calorie_burn_info() + " " + self.populate_calorie_consumption_info()
    from datetime import datetime

    @staticmethod
    def calculate_age(birthdate):
        today = datetime.now()
        try:
            birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
            age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
            return age
        except ValueError:
            return "Please enter the birthdate in the format YYYY-MM-DD"

    @staticmethod
    def year_or_years(age):
        if age == 1:
            return "year"
        else:
            return "years"


"""
a = UserInfo(1)
a.set_user_name("John Doe")
a.set_user_birthdate("1990-01-01")
a.set_user_height(180)
a.set_user_weight(80)
a.set_user_daily_calorie_intake(2000)
a.set_user_daily_calorie_burn(2500)
print(a.populate_user_info())
"""