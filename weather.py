import requests


def convert_to_celsius(temp_fahrenheit):
    # Formula to convert Fahrenheit to Celsius: Celsius = (Fahrenheit - 32) * 5/9
    # temp_celsius = (temp_fahrenheit - 32) * 5 / 9
    # temp_celsius = (temp_celsius - 32) * 5 / 9
    return temp_fahrenheit


class Weather(object):
    def __init__(self):
        self.API_KEY = "4432e3ca87b75ea276b4c5560f2373d3"
        self.BASE_URL = "http://api.openweathermap.org/data/2.5/weather/"

    def get_weather(self, city):
        URL = f"{self.BASE_URL}?q={city}&appid={self.API_KEY}&units=metric"
        print(URL)

        response = requests.get(URL)

        if response.status_code == 200:
            data = response.json()
            print(data)
            return data
            # weather_info = {
            #     "name": data["name"],
            #     "temp": convert_to_celsius(data["main"]["temp"]),
            #     "pressure": data["main"]["pressure"],
            #     "humidity": data["main"]["humidity"],
            # }
            # print(weather_info)
            # main_weather = data["weather"][0]["main"]
            # description = data["weather"][0]["description"]
            # temp = data["main"]["temp"]

            # return (
            #     f"Weather in {city}: {main_weather}\n{description}  Temperature: {temp}°F",
            #     weather_info,
            # )


        else:
            print(f"Error: {response.status_code}")


if __name__ == "__main__":
    weather = Weather()
    print(weather.get_weather("Vadodara"))
    # print(weather.get_weather("HYDERABAD"))
