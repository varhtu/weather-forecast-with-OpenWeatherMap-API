import requests
import json
import datetime

while True:
    print("...")
    print("...")
    print("...")
    print("****************************************")
    print(" Weather: South Kensington, London, UK")
    print("****************************************")
    print("...")
    print("...")
    print("...")


    #my_function = unix_time_converter
    def unix_timestamp_converter(self):
        inputtime = datetime.datetime.fromtimestamp(int(self)).strftime('%Y-%m-%d %H:%M:%S')
        return inputtime

    #my_function = unix_time_converter
    def unix_timestamp_converter2(self):
        inputtime2 = datetime.datetime.fromtimestamp(int(self)).strftime('%H:%M')
        return inputtime2

    #my rain_intensity function:
    def rain_intensity(self):


        if self == 0:
            intensity = "No rain"
        elif self <= 2.5:
            intensity = "Light"
        elif self <= 10:
            intensity = "Moderate"
        elif self <= 50:
            intensity = "Heavy"
        else:
            intensity = "Violent"

        return intensity

    #API guide --> https://openweathermap.org/api/one-call-api
    #API key = c8e7aa1f8c2885711137d08c53f24d23
    #request URL template --> https://api.openweathermap.org/data/2.5/onecall?lat=  {lat}  &lon=  {lon}  &exclude=  {part}  &appid=  {API key}


    endpoint = ("https://api.openweathermap.org/data/2.5/onecall?lat=51.4945386&lon=-0.1945962&exclude=alert&appid=********************************************************************&units=metric")
    #print("Retrieving OpenWeaterMap data from: ", endpoint)
    data = requests.get(endpoint)


    #convert data into json format
    allweatherdata = data.json()

    #print(allweatherdata)

    userinput = input('''

    Choose weather forecast:

    current / minutely / 12h / 7d

    User input:
    ''')
    if userinput == "current":
        print("-----------------------------------------------------------------------------------------------")
        print("CURRENT WEATHER")
        print("")
        currentweather = allweatherdata['current']
        #print(currentweather)
        print("Current time: ", unix_timestamp_converter(currentweather['dt']))
        print("")
        print("Current temperature:  ", round(currentweather['temp'], 1))
        print("Current weather:  ", currentweather['weather'][0]['description'])
        print("Wind speed:  ", currentweather['wind_speed'], "m/s")
        print("")
        print("Sunrise time:  ", unix_timestamp_converter(currentweather['sunrise']))
        print("Sunset time:  ", unix_timestamp_converter(currentweather['sunset']))
        print("")
        print("-----------------------------------------------------------------------------------------------")

    if userinput == "12h":
        print("-----------------------------------------------------------------------------------------------")
        print("12 HOUR WEATHER FORECAST")
        print("")
        hourlyweather = allweatherdata['hourly']
        #print(hourlyweather)
        for line in hourlyweather[1:13]:
            print("Time: ", unix_timestamp_converter(line['dt']))
            print("Temperature:  ", round(line['temp'], 1))
            print("Weather:  ", line['weather'][0]['description'])
            print("Chance of Rain:  ", line['pop']*100, "%")
            print("")
        print("-----------------------------------------------------------------------------------------------")

    if userinput == "minutely":
        print("-----------------------------------------------------------------------------------------------")
        print("MINUTELY WEATHER FORECAST - CHANCE OF RAIN")
        print("")
        minutelyweather = allweatherdata['minutely']
        #print(minutelyweather)
        for line in minutelyweather:
            print("Time: ", unix_timestamp_converter2(line['dt']))
            print("Rain intensity: ", rain_intensity(line['precipitation']), "(",round(line['precipitation'], 1),"mm )")
            print("")
        print("-----------------------------------------------------------------------------------------------")

    if userinput == "7d":
        print("-----------------------------------------------------------------------------------------------")
        print("7 DAY WEATHER FORECAST")
        print("")

        dailyweather = allweatherdata['daily']
        #print(dailyweather)
        for line in dailyweather:
            print("Date: ", unix_timestamp_converter(line['dt']))
            print("Daytime Temperature:  ", round(line['temp']['day'], 1))
            print("Nighttime Temperature:  ", round(line['temp']['night'], 1))
            print("Weather:  ", line['weather'][0]['description'])
            print("Chance of Rain:  ", line['pop']*100, "%")
            print("")
        print("-----------------------------------------------------------------------------------------------")
