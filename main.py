import requests


API_KEY="ebe9e119df4cd1b1ec52c4864d2ae8f4"
LAT=22.279800
LON=114.183937
UNITS="metric"
response=requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={LAT}&lon={LON}&appid={API_KEY}&units={UNITS}")

weathter_data=response.json()
clouldness= []
for i in range(0,48):
    weather=(weathter_data["hourly"][i]["weather"])
    clouldness.append(weather)

    if clouldness[i][0]["id"]!=800:
        print("not clear sky")
    else:
        print("clear sky")

