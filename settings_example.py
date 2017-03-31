# Change zip code in the below url to desired location
weather_url = "http://api.wunderground.com/api/2c8883d85ca5d155/forecast/q/12748.json"
from_email = "sending_email@gmail.com"
from_email_password = "password_here"
to_email = "receiving_email@gmail.com"
smtp_server = "smtp.gmail.com"  # Change if you're not using gmail
smtp_port = 587  # May need to change if you're not using gmail
forecast_days = (0, 1)  # Days to get weather (0 = today, 1 = tomorrow, etc.)
log_file = "log.txt"
