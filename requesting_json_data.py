#https://www.weatherapi.com/my/   # THis is the weather page where the information is pulled from
# 
#https://www.weatherapi.com/api-explorer.aspx 
import requests
city = input('What is the name of the city you are looking for the information ? \n')
url = 'http://api.weatherapi.com/v1/current.json?key=039ed970b48a446793850746230911&q='+city+'&aqi=no' # this link is gotten from https://www.weatherapi.com/api-explorer.aspx after creating a free account
response = requests.get(url)
weather_json = response.json()
temp = weather_json.get('current').get('temp_f') # current is a field in the above URL json format
                                            # temp_f is the tempaature if 'F' in the json format in the url file above
place = weather_json.get('location').get('country')
description =weather_json.get('current').get('condition').get('text')

print("Today's weather in", city,  'is', description, 'and', temp, 'degrees', 'and the  country is', place.upper() )
