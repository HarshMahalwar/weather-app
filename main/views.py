from django.shortcuts import render, redirect
import requests


# Create your views here.

def github():
    return redirect('https://github.com/HarshMahalwar?tab=repositories')


def linkedin():
    return redirect('https://www.linkedin.com/in/harsh-mahalwar-4310b316a/')


def weather(request):
    bool1 = False
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    API_KEY = '062097d003a0c38cf0565507120e4349'
    if request.method == 'POST':
        CITY = request.POST['city']
        URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
        response = requests.get(URL)
        if response.status_code == 200:
            data = response.json()
            main = data['main']
            report = data['weather']
            temp = int(main['temp']) - 273
            temp_min = int(main['temp_min']) - 273
            temp_max = int(main['temp_max']) - 273
            feels_like = int(main['feels_like']) - 273
            bool1 = True
            context = {
                'feels_like': feels_like,
                'main': main,
                'city': CITY,
                'temp_min': temp_min,
                'temp_max': temp_max,
                'temp': temp,
                'report': report,
                'bool': bool1
            }
            return render(request, 'home.html', context)
    return render(request, 'home.html')