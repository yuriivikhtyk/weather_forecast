import requests
import smtplib

key = 'your_api_openweather_key'

parameters = {
  'lat' : '51.246910',
  'lon' : '22.573620',
  'appid' : key
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()


weather_id = []
weather_description = []
for i in data["list"]:
    id = i["weather"][0]["id"]
    weather_id.append(id)
    descr = i["weather"][0]["main"]
    weather_description.append(descr)


my_email = "your_email@gmail.com"
my_password = "app_password"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs=my_email, 
        msg=f"Subject:Weather forecast\n\nNow is expected the weather {weather_id[0]}, {weather_description[0]}.\nIn 3 hours is expected: {weather_id[1]}, {weather_description[1]}.\nIn 6 hours is expected: {weather_id[2]}, {weather_description[2]}.\nIn 9 hours is expected: {weather_id[3]}, {weather_description[3]}.\nIn 12 hours is expected: {weather_id[4]}, {weather_description[4]}.\n"
        )

msg=f"Subject:Weather forecast\n\nNow is expected the weather {weather_id[0]}, {weather_description[0]}.\nIn 3 hours is expected: {weather_id[1]}, {weather_description[1]}.\nIn 6 hours is expected: {weather_id[2]}, {weather_description[2]}.\nIn 9 hours is expected: {weather_id[3]}, {weather_description[3]}.\nIn 12 hours is expected: {weather_id[4]}, {weather_description[4]}.\n"
print(msg)