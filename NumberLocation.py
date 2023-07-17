import phonenumbers

import folium

from MyNumber import number

from phonenumbers import geocoder


yournumber = phonenumbers.parse(number)

yourlocation = geocoder.description_for_number(yournumber,"en")

print(yourlocation)

# Service Provider

from phonenumbers import carrier

#service_provider = phonenumbers.parse(number)

service_provider_name = carrier.name_for_number(yournumber,"en")

print(service_provider_name)

#To get Latitude and Longatude from map

from opencage.geocoder import OpenCageGeocode

key = "5ae152dd60f04231ac2488808970f2cd"

geocoder = OpenCageGeocode(key)

quary = str(yourlocation)

result = geocoder.geocode(quary)

# print(result) we need only latitude and longatude

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']

print(lat,lng)

myMap = folium.Map(location=[lat, lng],zoom_start=9)

folium.Marker([lat,lng],popup=yourlocation).add_to(myMap)

#save in html file

myMap.save("myLocation.html")