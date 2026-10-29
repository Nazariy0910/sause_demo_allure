weather_response = {
 "city": "Prague",
 "temperature": 15.5,
 "status": "Cloudy",
 "history":["Monday: 12", "Tuesday: 14", "Wednesday: 15.5"]
}

city= weather_response['city']
temp= weather_response["temperature"]
print(f'Weather in {city}: {temp} degrees')

weather_final = weather_response["history"][2]
print(f"Yesterday was: {weather_final}")
  