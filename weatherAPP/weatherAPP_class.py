import requests

class WeatherApp:
    def __init__(self):
        self.api_key = "1b6cb79e8dfe4a76aa9151908242907"
        self.city = None

    def set_city(self):
        while True:
            try:
                print("--------------API OpenWeatherMap--------------")
                city = input("Enter city: ")
                if city:
                    self.city = city
                    return city
                else:
                    print("City name cannot be empty. Please try again.")

            except KeyboardInterrupt:
                    print("\nInput was interrupted.")
                    return None
            except Exception as e:
                print(f"An error occurred: {e}")
            return None

    def check_data(self):
        url = 'http://api.weatherapi.com/v1/current.json'
        params = {'key': self.api_key, 'q': self.city, 'aqi': 'no'}

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()

        except requests.exceptions.HTTPError:
            if response.status_code == 400:
                print(f"Error - City '{self.city}' not found. Please try again.")
                self.set_city()
                return self.check_data()
            else:
                print(f"HTTP error: {response.status_code}. Please try again.")

        except requests.exceptions.RequestException as e:
            print(f"Connection error: {e}. Please check your internet and try again.")

    def display_weather(self, info):
        if not info:
            return

        # print(response.json()
        print(f"City: {info['location']['name']}, Country: {info['location']['country']}\nLocal time: {info['location']['localtime']}")
        print(f"Temp in C: {info['current']['temp_c']}, Temp in F: {info['current']['temp_f']}, Condition: {info['current']['condition']['text']}")
        print(f"Wind {info['current']['wind_kph']} km/h, Humidity: {info['current']['humidity']}%")

    def run(self):

        self.set_city()
        info = self.check_data()
        self.display_weather(info)

if __name__ == '__main__':
    app = WeatherApp()
    app.run()