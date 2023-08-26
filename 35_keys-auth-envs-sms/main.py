import requests
from twilio.rest import Client

# Weather API
OWM_endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "redacted"

# Twilio API
account_sid = 'ACc07f3c9a7c4e5ce40f6b526f47910914'
auth_token = 'redacted'

weather_params = {
    "lat": 43.0722,
    "lon": -89.4008,
    "exclude": "current,minutely,daily",
    "APPID": api_key,
}

response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
weather_slice = weather_data["id"]
if weather_slice < 700:
        print("Bring an umbrella")
        will_rain = True
        
if True:
    client = Client(account_sid, auth_token)    
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an ☔️",
            from_="+18334032854",
            to="redacted"
        )
        
print(message.status)