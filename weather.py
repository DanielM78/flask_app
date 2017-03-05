import forecastio
from geopy.geocoders import Nominatim
import os 

from dotenv import load_dotenv, find_dotenv
<<<<<<< HEAD
load_dotenv(find_dotenv())

def get_weather(address):
    api_key = os.environ['FORECASTIO_API_KEY']
    geolocator = Nominatim()
    location = geolocator.geocode(address)
    latitude = location.latitude
    longitude = location.longitude
    forecast = forecastio.load_forecast(api_key, latitude, longitude).currently()
    summary = forecast.summary
    temperature = forecast.temperature
    return "{} and {}° at {}".format(summary, temperature, address)
=======

load_dotenv(find_dotenv())

def get_weather(address):
	api_key = os.environ['FORECASTIO_API_KEY']
	geolocator = Nominatim()
	location = geolocator.geocode(address)
	latitude = location.latitude
	longitude = location.longitude
	forecast = forecastio.load_forecast(api_key, latitude, longitude).currently()
	summary = forecast.summary
	temperature = forecast.temperature
	return "{} and {}° at {}".format(summary, temperature, address)
>>>>>>> 7da1378c68252e91871dbd6f3c82217ceb4a8953
