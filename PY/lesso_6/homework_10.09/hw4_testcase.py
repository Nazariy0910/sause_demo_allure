class TestCase:
    def __init__(self, name, expected):
        self.name = name
        self.expected = expected
        self.status = 'not run'
        self.actual = None

    def run(self, actual_result):
        self.actual = actual_result
        if actual_result == self.expected:
            self.status = 'passed'
        else:
            self.status = "failed"

    def print_result(self):
        if self.status == "passed":
            status_text = "✅ PASSED"
        elif self.status == "failed":
            status_text = "❌ FAILED"
        else:
            status_text = self.status

        print(f"Test:     {self.name}")
        print(f"Expected: {self.expected}")
        print(f"Actual:   {self.actual}")
        print(f"Status:   {status_text}\n") 


test1 = TestCase("Checking the button to open a window", "The button works a window opens")
test1.run("The button works a window opens") 

test2 = TestCase("Checking registration on WOLT website", "Registration successful")
test2.run("Login failed")

test3 = TestCase("API response status for data transfer", "200 OK")
test3.run("500 Server Error")

test1.print_result()
test2.print_result()
test3.print_result()

