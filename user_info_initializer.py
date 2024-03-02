import user_info

class Interactor:
    def __init__(self, user_id):
        self.user_info = user_info.UserInfo(user_id)

    def set_user_info(self, file_path):
        with open(file_path, "r") as file:
            lines = file.readlines()
            self.user_info.set_user_name(lines[0].strip())
            self.user_info.set_user_birthdate(lines[1].strip())
            self.user_info.set_user_height(int(lines[2].strip()))
            self.user_info.set_user_weight(int(lines[3].strip()))
            self.user_info.set_user_daily_calorie_intake(int(lines[4].strip()))
            self.user_info.set_user_daily_calorie_burn(int(lines[5].strip()))

    def add_user_questions(self, question):
        self.user_info.add_user_question(question)

    def get_prompt(self):
        return self.user_info.populate_user_info()