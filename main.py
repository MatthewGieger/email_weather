import smtplib
from urllib.request import urlopen
import json
import settings
import time

def get_weather_data(weather, day, indicator, unit=""):
    """ Gets weather data from parsed json
    Parameters:
        weather (dict): Weather data
        day (int): Day number (0 = Today, 1 = Tomorrow, etc.)
        indicator (str): Weather indicator (ie. 'high', 'maxwind', etc.)
        unit (str): Unit of measurement (it 'in', 'mph', etc.)

    Returns:
        (str): Value of weather data
    """
    if not(unit):
        return weather["forecast"]["simpleforecast"]["forecastday"][day][indicator]
    else:
        return weather["forecast"]["simpleforecast"]["forecastday"][day][indicator][unit]


response = urlopen(settings.weather_url)
weather = json.loads(response.read())

smtp_server = smtplib.SMTP(host=settings.smtp_server, port=settings.smtp_port)
smtp_server.ehlo()
smtp_server.starttls()
smtp_server.ehlo()
smtp_server.login(settings.from_email, settings.from_email_password)

for day in settings.forecast_days:
    max_temp = get_weather_data(weather, day, "high", "fahrenheit")
    min_temp = get_weather_data(weather, day, "low", "fahrenheit")
    max_wind = get_weather_data(weather, day, "maxwind", "mph")
    wind_dir = get_weather_data(weather, day, "maxwind", "dir")
    avg_humidity = get_weather_data(weather, day, "avehumidity")
    precip_percent = get_weather_data(weather, day, "pop")
    precip_amt = get_weather_data(weather, day, "qpf_allday", "in")
    subject = "Weather"
    weather_day = "Today" if day == 0 else "Tomorrow" if day == 1 else ""
    msg = "Good Morning Dad! Here's {weather_day}'s Weather: MaxTemp:{max_temp}  MinTemp:{min_temp}  MaxWind:{max_wind}  Humidity:{avg_humidity}  Precip%:{precip_percent}  PrecipAmt:{precip_amt}".format(
        weather_day=weather_day,
        max_temp=max_temp,
        min_temp=min_temp,
        max_wind=str(max_wind) + wind_dir,
        avg_humidity=avg_humidity,
        precip_percent=precip_percent,
        precip_amt=precip_amt
    )

    smtp_server.sendmail(
        settings.from_email,
        settings.to_email,
        subject + ":" + "\n\n" + msg
    )

smtp_server.quit()

# Log Process #
with open(settings.log_file, "a") as f:
    f.write(f"{time.strftime('%Y-%m-%d-%X')}: Email sent to {settings.to_email} from {settings.from_email}\n")
