weather_url = "http://api.wunderground.com/api/{key}/forecast/q/{zip}.json".format(
        key='weather_underground_api_key',  # get key: wunderground.com/weather/api/
        zip='13778')
from_email = "sending_email@gmail.com"  # The email you want to send from
from_email_password = "password_here"  # The sending email's password
to_email = "receiving_email@gmail.com"  # The email receiving the weather
smtp_server = "smtp.gmail.com"  # Change if you're not using gmail
smtp_port = 587  # May need to change if you're not using gmail
forecast_days = (0, 1)  # Days to get weather (0 = today, 1 = tomorrow, etc.)
log_file = "log.txt"
