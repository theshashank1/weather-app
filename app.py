from flask import Flask, render_template, request, url_for, redirect
from weather import Weather

app = Flask(__name__)


@app.route("/home")
def index():
    if "city" in request.args:
        city = request.args["city"]
        weather = Weather()
        info = weather.get_weather(city)
        return render_template("index.html", weather=info)
    return render_template(
        "index.html",
        weather=(
            "Weather in Hyderabad: Clouds\nscattered clouds  Temperature: 306.38°F",
            {"name": "Hyderabad", "temp": 306.38, "pressure": 1017, "humidity": 38},
        ),
    )


@app.route("/")
def home():
    if "city" in request.args:
        city = request.args["city"]
        weather = Weather()
        info = weather.get_weather(city)
        return render_template("weather.html", methods=["GET", "POST"], weather=info)

    else:
        return render_template(
            "weather.html",
            methods=["GET", "POST"],
            weather={
                "coord": {"lon": 73.2, "lat": 22.3},
                "weather": [
                    {"id": 711, "main": "Smoke", "description": "smoke", "icon": "50d"}
                ],
                "base": "stations",
                "main": {
                    "temp": 26.98,
                    "feels_like": 26.33,
                    "temp_min": 26.98,
                    "temp_max": 26.98,
                    "pressure": 1015,
                    "humidity": 28,
                },
                "visibility": 5000,
                "wind": {"speed": 1.54, "deg": 160},
                "clouds": {"all": 2},
                "dt": 1710823313,
                "sys": {
                    "type": 1,
                    "id": 9060,
                    "country": "IN",
                    "sunrise": 1710810726,
                    "sunset": 1710854266,
                },
                "timezone": 19800,
                "id": 1253573,
                "name": "Vadodara",
                "cod": 200,
            },
        )


if __name__ == "__main__":
    app.run(debug=True)
