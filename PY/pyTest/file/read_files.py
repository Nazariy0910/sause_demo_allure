import json

# # file = open('my_log.txt', 'w') перший варіант для створення записі
# # file.write('Test aprove\n')
# # file.close()

# with open('my_log.txt', 'a') as f:
#     f.write('Test aprove\n')
#     f.write('Test failed\n')  новий метод для записі

# print('File saved and closed')

# with open('my_log.txt', 'r') as f:
#     content = f.read()
#     print(content)

# with open('my_log.txt', 'r') as f:
#     count = 1
#     for line in f:
#         print(f'{count} - {line.strip()}')
#         count +=1

# server_response = """
# {
#     "city": "Prague",
#     "temperature": 15.5,
#     "is_raining": false,
#     "wind": null
# }
# """

# weather = json.loads(server_response)
# print(weather['city'])
# print(weather['temperature'])
# print(weather['wind'])
# print(type(weather))


# new_user = {
#     "login": "qa_ninja",
#     "password": "secret123",
#     "is_admin": True,
#     "avatar": None
# }

# json_strip = json.dumps(new_user, indent=4)
# print(type(json_strip))
# print(json_strip)

test_results = {
    "test_login": "Passed",
    "test_cart":  "Failed",
    "total_bugs": 1
}

print(f'test_result = {type(test_results)}')

with open('report.json', 'w') as f:
    json.dump(test_results,f , indent=4 )

print('save report')

with open('report.json', 'r') as f:
    loaded = json.load(f)

print (loaded['test_login'])
print (loaded['test_cart'])