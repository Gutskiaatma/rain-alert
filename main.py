import requests
from twilio.rest import Client




account_sid = "ACc0daca9abdef992aefead7ee28b6e6af"
auth_token = "dd8b9898f48bcabf99542225edc96006"



omw_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "ee7974f4602a36986cd87903686e5dee"
lat = 15.351400
lon = 75.147600
parameters = {
    "lat":lat,
    "lon":lon,
    "appid":api_key,
    "cnt":4

}

reponse = requests.get(omw_endpoint, params=parameters)
print(reponse.status_code)
reponse.raise_for_status()
data = reponse.json()
# print(data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today bring the ☂ ☔ ",
        from_='+17472988928',
        to='+919829143004'
    )

    print(message.sid)