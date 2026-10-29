class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.is_active = True

    def login(self):
        print(f'{self.name} add to system')

    def logout(self):
            print(f'{self.name} add to system')

    def get_info(self):
            print(f'{self.name} ({self.email})')


class AdminUser(User):
    def __init__(self, name, email, departmen):
            self.name = name
            self.email = email
            self.is_active = True
            self.departmen = departmen
            self.permission = []

    def grant_permission(self, permission):
        self.permission.append(permission)
        print(f"{self.name}")

    def delete_user(self,target_user):
        print(f'{self.name} {target_user.name}')

    def get_info(self):
          print(f'administrator{self.name} ({self.email}) | {self.departmen}')


regular = User("iva","ivan@test.com")
admin = AdminUser("ivan","ivan@test.com",departmen="QA")

regular.get_info
regular.get_info()


admin.login()
admin.grant_permission('delete')
admin.grant_permission('view')
admin.delete_user(regular)
admin.get_info()