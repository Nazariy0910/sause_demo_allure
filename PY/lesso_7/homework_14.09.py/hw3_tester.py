class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.__login_count = 0

    def login(self):
        self.__login_count += 1
        print(f"{self.name} has logged in’")

    def logout(self):
        print(f"{self.name} has logged out")

    def get_login_count(self):
        return self.__login_count

    def get_info(self):
        print(f"User{self.name} | Email: {self.email} | Login: {self.__login_count}")

class Tester(User):
    def __init__(self, name, email, level):
        self.name = name
        self.email = email
        self.level = level
        self.__bugs = []
        self.__login_count = 0 

    def login(self):
        self.__login_count += 1
        print(f"{self.name} ({self.level}) has logged in")

    def report_bug(self,bug):
        self.__bugs.append(bug)
        print(f"Bug detected: {bug}")

    def get_bugs(self):
        return self.__bugs

    def get_info(self):
        print(
            f"Пользователь: {self.name} | "
            f"Email: {self.email} | "
            f"Уровень: {self.level} | "
            f"Входов: {self.__login_count} | "
            f"Багов найдено: {len(self.__bugs)}"
        )

user = User("Ivan", "ivan@test.com")
user.login()
user.login()
user.get_info()

print()

tester = Tester("Anna", "anna@test.com", "middle")
tester.login()
tester.login()
tester.login()

tester.report_bug("кнопка не кликается")
tester.report_bug("страница не загружается")

tester.get_info()