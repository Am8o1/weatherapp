import requests

def get_weather(api_key, city):
    base_url = "http://api.weatherstack.com/current"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data["cod"] == 200:
            weather_info = {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"].capitalize(),
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"]
            }
            return weather_info
        else:
            return None
    except requests.exceptions.RequestException as e:
        print("Error connecting to the weather service:", e)
        return None
    
def display_weather(weather_info):
    if weather_info is None:
        print("City not found or an error occurred.")
    else:
        print("Weather in {}: ".format(weather_info["city"]))
        print("Temperature: {}°C".format(weather_info["temperature"]))
        print("Description: {}".format(weather_info["description"]))
        print("Humidity: {}%".format(weather_info["humidity"]))
        print("Wind Speed: {} m/s".format(weather_info["wind_speed"]))

def main(api_key):
    api_key = "da4311d571ec284e436cbc3b525708c4"
    city = input("Enter the city name: ")

    weather_info = get_weather(api_key, city)
    display_weather(weather_info)

if __name__ == "__main__":
    main("da4311d571ec284e436cbc3b525708c4")
