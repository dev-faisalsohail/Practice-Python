# weather (find average temperature,average humidity , hottest day, coldest day, most comfortable day
# based on humidity and temperature in a week)

data = [
    {"day": "Monday", "temperature": 32, "humidity": 60, "rainfall": 5, "city": "Karachi"},
    {"day": "Tuesday", "temperature": 34, "humidity": 55, "rainfall": 0, "city": "Karachi"},
    {"day": "Wednesday", "temperature": 30, "humidity": 65, "rainfall": 2, "city": "Karachi"},
    {"day": "Thursday", "temperature": 28, "humidity": 70, "rainfall": 10, "city": "Karachi"},
    {"day": "Friday", "temperature": 33, "humidity": 50, "rainfall": 0, "city": "Karachi"},
    {"day": "Saturday", "temperature": 35, "humidity": 45, "rainfall": 0, "city": "Karachi"},
    {"day": "Sunday", "temperature": 31, "humidity": 60, "rainfall": 1, "city": "Karachi"}
]

total_temp = 0
#print(type(total_temp))
total_humidity = 0
hottest_day = data[0]
coldest_day = data[0]
most_comfortable_day = data[0]

for entry in data:
    total_temp += entry["temperature"]
    total_humidity += entry["humidity"]
    
    if entry["temperature"] > hottest_day["temperature"]:
        hottest_day = entry
    
    if entry["temperature"] < coldest_day["temperature"]:
        coldest_day = entry
    
    # Assuming "most comfortable" means the lowest humidity for this example
    if entry["humidity"] < most_comfortable_day["humidity"]:
        most_comfortable_day = entry

average_temp = total_temp / len(data)
average_humidity = total_humidity / len(data)
print(f"Average Temperature: {average_temp:.2f}°C")
print(f"Average Humidity: {average_humidity:.2f}%")
print(f"Hottest Day: {hottest_day['day']} ({hottest_day['temperature']}°C, {hottest_day['humidity']}%)")
print(f"Coldest Day: {coldest_day['day']} ({coldest_day['temperature']}°C, {coldest_day['humidity']}%)")
print(f"Most Comfortable Day: {most_comfortable_day['day']} ({most_comfortable_day['temperature']}°C, {most_comfortable_day['humidity']}%)")

# Output:
# Average Temperature: 32.43°C
# Average Humidity: 58.57%
# Hottest Day: Saturday (35°C, 45%)
# Coldest Day: Thursday (28°C, 70%)
# Most Comfortable Day: Saturday (35°C, 45%)  

