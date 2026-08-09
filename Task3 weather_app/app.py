import requests


API_KEY = "91c7c087bbd49daa8df0ce483a6eca75"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)

        if response.status_code == 404:
            print("City not found. Please check the city name.")
            return

        response.raise_for_status()

        data = response.json()

        city_name = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]

        print("\n" + "=" * 35)
        print("        WEATHER INFORMATION")
        print("=" * 35)
        print(f"City        : {city_name}, {country}")
        print(f"Temperature : {temperature}°C")
        print(f"Humidity    : {humidity}%")
        print(f"Condition   : {description.title()}")
        print("=" * 35)

    except requests.exceptions.RequestException as error:
        print("Error connecting to the weather service.")
        print(f"Details: {error}")


def main():
    print("================================")
    print("       WEATHER APP")
    print("================================")

    city = input("Enter city name: ").strip()

    if not city:
        print("Please enter a city name.")
        return

    get_weather(city)


if __name__ == "__main__":
    main()