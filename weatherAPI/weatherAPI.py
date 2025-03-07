import requests

def set_city():
    while True:
        try:
            print("API OpenWeatherMap")
            user_input = input("Enter city: ")
            if user_input:
                return user_input
            else:
                print("City name cannot be empty. Please try again.")

        except KeyboardInterrupt:
            print("\nInput was interrupted.")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

def check_data(city, api_key):
    url = 'http://api.weatherapi.com/v1/current.json'
    while True:
        params = {
        'key': api_key,
        'q': city,
        'aqi': 'no'
    }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()

        except requests.exceptions.HTTPError:
            if response.status_code == 400:
                print(f"Error - City '{city}' not found. Please try again.")
                city = set_city()
            else:
                print(f"HTTP error: {response.status_code}. Please try again.")

        except requests.exceptions.RequestException as e:
            print(f"Connection error: {e}. Please check your internet and try again.")

def main():
    api_key = "1b6cb79e8dfe4a76aa9151908242907"
    city = set_city()

    info = check_data(city, api_key)
    if not info:
        return

    # print(response.json())

    print(f"City: {info['location']['name']}, Country: {info['location']['country']}\nLocal time: {info['location']['localtime']}")
    print(f"Temp in C: {info['current']['temp_c']}, Temp in F: {info['current']['temp_f']}, Condition: {info['current']['condition']['text']}")
    print(f"Wind {info['current']['wind_kph']} km/h, Humidity: {info['current']['humidity']}%")

if __name__ == '__main__':
    main()