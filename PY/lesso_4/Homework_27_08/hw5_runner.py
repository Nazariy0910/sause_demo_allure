from os import name
import random
import time

test_cases = [
    'Go to the home page',
    'Log in',
    'Add to basket',
    'Proceed to checkout',
    'Log out'
]

def run_test(name):
    return name

for i in test_cases:
    new_result= run_test(i)


def run_test(test_name):
    time.sleep(1)  
    return random.choice(["passed", "failed"])

passed_count = 0
failed_count = 0

print("🚀 Running test suite...\n")


for test in test_cases:
    result = run_test(test)
    
    if result == "passed":
        passed_count += 1
        print(f"✅ PASSED: {test}")
    else:
        failed_count += 1
        print(f"❌ FAILED: {test}")

print("📊 ИТОГОВЫЙ ОТЧЕТ")
print(f"Total tests: {len(test_cases)}")
print(f"Successful (Passed): {passed_count}")
print(f"Failed: {failed_count}")