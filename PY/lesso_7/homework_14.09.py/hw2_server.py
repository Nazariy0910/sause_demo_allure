class Server:
    def __init__ (self, host, port, password):
        self.host = host
        self.port = port
        self.__password = password

    def check_password(self, input_password):
        if input_password == self.__password:
            return True
        else:
            False

    def get_adress(self):
        return (f"{self.host}:{self.port}")

    def describe(self):
        print(self.get_adress())

class TestServer(Server) :
    def __init__ (self, host, port, password, enviorment ):
        self.host = host
        self.port = port
        self._Server__password = password
        self.environment = enviorment
        self.__logs = []

    def log(self, message):
        self.__logs.append(message)
        print(f"{self.environment} LOG: {message}")
        
    def get_logs(self):
        return self.__logs

    def describe(self):
        print(
            f"Adress: {self.get_adress()} | "
            f"Environment: {self.environment} | "
            f"Логов: {len(self.__logs)}"
        )

server = Server("prod.myshop.cz", 443, "secret123")
server.describe()
print(f"Password is wrong: {server.check_password('secret123')}")
print(f"Password is wrong: {server.check_password('wrong_pass')}")

print()

test_server = TestServer("staging.myshop.cz", 8080, "test1234", "staging")

print(test_server.get_adress())
print(f"Окружение: {test_server.environment}")
print(f"Логов: {len(test_server.get_logs())}")

test_server.log("running the test")
test_server.log("Login was successful")
test_server.log("Test failed: button not found")

test_server.describe()