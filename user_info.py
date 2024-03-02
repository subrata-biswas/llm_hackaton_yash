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

    def populate_user_info(self):
        age = self.calculate_age(self.get_user_birthdate())
        return f"We have a {age} {self.year_or_years(age)} old patient"

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




