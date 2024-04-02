import urllib.request
import json
from django.shortcuts import render

# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&APPID=22d1bbf9c7242d2893264c2acb48a8e9').read()
        key_data = json.loads(res)
        weather_status ={
            "Temperature": str(key_data['main']['temp']),
            "Humidity": str(key_data['main']['humidity']),
            "Pressure": str(key_data['main']['pressure']),
            "Id": str(key_data['weather'][0]['id']),
            "Description": str(key_data['weather'][0]['description']),
            "Icon": str(key_data['weather'][0]['icon']), 
        }

    else:
        city = ''
        weather_status = {}  
    return render(request, 'index.html', {'city': city, 'weather_status': weather_status} )
