# status_code = int(input("Enter status code: "))
# if status_code == 200:
#     print("✅ OK. The request has been successfully completed.")
# elif status_code == 201:
#     print("✅ Created. The request has been successfully completed.")
# elif status_code == 400:
#     print("❌ Bad Request. The request could not be understood.")
# elif status_code == 401:
#     print("❌ Unauthorized. Please authenticate.")
# elif status_code == 404:
#     print("❌ Not Found. The requested resource was not found.")
# elif status_code == 500:
#     print("❌ Internal Server Error. An error occurred on the server.")
# else:
#     print("❌ Unknown Status Code. Please check the status code.")

status_code = int(input("Введите статус-код: "))

statuses = {
    200: "✅ OK. Запрос выполнен успешно.",
    201: "✅ Created. Resource created",
    400: "❌ Bad Request. Invalid request",
    401: "❌ Unauthorised. Authorisation required.",
    404: "❌ Not Found. Страница не найдена.",
    500: "💥 Internal Server Error. Сервер сломался."
}

message = statuses.get(status_code, "❓ Неизвестный статус-код.")
print(message)