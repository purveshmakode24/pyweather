import requests
import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def weather(request):
    # your API key goes in appid filed :)
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=************************'
    location = 'Delhi'
    r = requests.get(url.format(location)).json()
    print(r)
    dict1 = {
        # 'location': location,
        'temperature': r['main']['temp'],
        # 'description': r['weather'][0]['description'],
        # 'icon': r['weather'][0]['icon'],
        # 'wind_speed': r['wind']['speed'],
        # 'humidity': r['main']['humidity'],
        # 'wind_deg': r['wind']['deg'],
        # 'time_of_data_cal': r['dt'],

        # 'red1': 'Precautions and Carries to be taken at this place in this week.' if 'temperature' < '20' else 'Precautions and Carries to be taken at this place in this week.',
        # 'red2': 'The place is enough cold to make you sick.' if 'temperature' < '20' else 'The place has high temperature. Bad atmospheremmay damage skin.',
        # 'red3': 'Carry warm clothes with you.' if 'temperature' < '20' else 'Wear cotton clothes. Loose clothes made of linen would be very comfortable.',
        # 'red4': 'Sudden temperature change may cause your health to spoil.' if 'temperature' < '20' else 'No environment for tourism or sight-seeing.',

    }

    print(dict1)
    # t = 'temperature'
    # print(dict1.get(t))

    # if dict1.get(t) < 20:
    #     dict2 = {
    #         'red1': 'Danger',
    #         'red2': 'Be Careful',
    #         'red3': 'Hell',
    #     }
    # else:
    #     dict2 = {
    #         'red1': 'abovee 20',
    #         'red2': 'ldflksdf',
    #         'red3': 'zxczxczxczxcz',
    #     }
    #     a = 'red1'
    #     print(dict2.get(a))

    if dict1['temperature'] <= 10:
        dict1 = {
            'red1': 'Precautions and Carries must be taken at this place in this week.',
            'red2': 'The place is enough cold to make you sick.',
            'red3': 'Carry warm clothes with you.',
            'red4': 'Sudden temperature change may cause your health to spoil.',
            'red5': 'Do not smoke or drink alcohol; neither will warm you up. On the contrary, smoking or drinking alcohol may lower your body temperature even more and lead to \'hypothermia\'.',
            'location': location,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
            'wind_speed': r['wind']['speed'],
            'humidity': r['main']['humidity'],
            'temp_max': r['main']['temp_max'],
            'day_of_cal': datetime.datetime.fromtimestamp(r['dt']).strftime('%A'),
            'date_month_of_cal': datetime.datetime.fromtimestamp(r['dt']).strftime("%d %b"),
        }
    elif dict1['temperature'] > 10 and dict1['temperature'] <= 20:
        dict1 = {
            'red1': 'Precautions and Carries must be taken at this place in this week.',
            'red2': 'The place has low temperature. Good weather, soothing air for sight-seeing.',
            'red3': 'Not necessary but still carry extra clothes to warm you up.',
            'red4': 'Sudden temperature change may cause your health to spoil.',
            'red5': 'Do not stay outside too long without being well protected from the cold.',
            'location': location,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
            'wind_speed': r['wind']['speed'],
            'humidity': r['main']['humidity'],
            'temp_max': r['main']['temp_max'],
            'day_of_cal': datetime.datetime.fromtimestamp(r['dt']).strftime('%A'),
            'date_month_of_cal': datetime.datetime.fromtimestamp(r['dt']).strftime("%d %b"),
        }
    elif dict1['temperature'] > 20 and dict1['temperature'] <= 38:
        dict1 = {
            'red1': 'Precautions and Carries must be taken at this place in this week.',
            'red2': 'The place has medium temperature. Good weather, but humidity is more.',
            'red3': 'No extra clothing demands. Normal ones would be good. Woah!',
            'red4': 'Temperature is normal. No need to worry.',
            'red5': 'Wear cotton clothes or light woolens.',
            'location': location,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
            'wind_speed': r['wind']['speed'],
            'humidity': r['main']['humidity'],
            'temp_max': r['main']['temp_max'],
            'day_of_cal': datetime.datetime.fromtimestamp(r['dt']).strftime('%A'),
            'date_month_of_cal': datetime.datetime.fromtimestamp(r['dt']).strftime("%d %b"),
        }
    else:
        dict1 = {
            'red1': 'Precautions and Carries must be taken at this place in this week.',
            'red2': 'The place has high temperature. Bad atmosphere may damage skin.',
            'red3': 'Wear cotton clothes. Loose clothes made of linen would be very comfortable.',
            'red4': 'No environment for tourism or sight-seeing.',
            'red5': 'Drink water, even if you don’t feel thirsty. Take a bottle with you always.',
            'location': location,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
            'wind_speed': r['wind']['speed'],
            'humidity': r['main']['humidity'],
            'temp_max': r['main']['temp_max'],
            'day_of_cal': datetime.datetime.fromtimestamp(r['dt']).strftime('%A'),
            'date_month_of_cal': datetime.datetime.fromtimestamp(r['dt']).strftime("%d %b"),
        }
    print(dict1)
    return render(request, 'index.html', dict1)


def weather_details(request):
    if request.method == 'POST':
        url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=66b1fdc61a1a4198702b3fafc52537b2'
        location = request.POST.get('city')
        r = requests.get(url.format(location)).json()
        print(r)
        dict1 = {
            # 'location': location,
            'temperature': r['main']['temp'],
            # 'description': r['weather'][0]['description'],
            # 'icon': r['weather'][0]['icon'],
            # 'wind_speed': r['wind']['speed'],
            # 'humidity': r['main']['humidity'],
            # 'wind_deg': r['wind']['deg'],
            # 'time_of_data_cal': r['dt'],

            # 'red1': 'Precautions and Carries to be taken at this place in this week.' if 'temperature' < '20' else 'Precautions and Carries to be taken at this place in this week.',
            # 'red2': 'The place is enough cold to make you sick.' if 'temperature' < '20' else 'The place has high temperature. Bad atmosphere may damage skin.',
            # 'red3': 'Carry warm clothes with you.' if 'temperature' < '20' else 'Wear cotton clothes. Loose clothes made of linen would be very comfortable.',
            # 'red4': 'Sudden temperature change may cause your health to spoil.' if 'temperature' < '20' else 'No environment for tourism or sight-seeing.',

        }
        print(dict1)

        if dict1['temperature'] <= 10:
            dict1 = {
                'red1': 'Precautions and Carries must be taken at this place in this week.',
                'red2': 'The place is enough cold to make you sick.',
                'red3': 'Carry warm clothes with you.',
                'red4': 'Sudden temperature change may cause your health to spoil.',
                'red5': 'Do not smoke or drink alcohol; neither will warm you up. On the contrary, smoking or drinking alcohol may lower your body temperature even more and lead to \'hypothermia\'.',
                'location': location,
                'temperature': r['main']['temp'],
                'description': r['weather'][0]['description'],
                'icon': r['weather'][0]['icon'],
                'wind_speed': r['wind']['speed'],
                'humidity': r['main']['humidity'],
                'temp_max': r['main']['temp_max'],
                'day_of_cal': datetime.datetime.fromtimestamp(r['dt']).strftime('%A'),
                'date_month_of_cal': datetime.datetime.fromtimestamp(r['dt']).strftime("%d %b"),
            }
        elif dict1['temperature'] > 10 and dict1['temperature'] <= 20:
            dict1 = {
                'red1': 'Precautions and Carries must be taken at this place in this week.',
                'red2': 'The place has low temperature. Good weather, soothing air for sight-seeing.',
                'red3': 'Not necessary but still carry extra clothes to warm you up.',
                'red4': 'Sudden temperature change may cause your health to spoil.',
                'red5': 'Do not stay outside too long without being well protected from the cold.',
                'location': location,
                'temperature': r['main']['temp'],
                'description': r['weather'][0]['description'],
                'icon': r['weather'][0]['icon'],
                'wind_speed': r['wind']['speed'],
                'humidity': r['main']['humidity'],
                'temp_max': r['main']['temp_max'],
                'day_of_cal': datetime.datetime.fromtimestamp(r['dt']).strftime('%A'),
                'date_month_of_cal': datetime.datetime.fromtimestamp(r['dt']).strftime("%d %b"),
            }
        elif dict1['temperature'] > 20 and dict1['temperature'] <= 38:
            dict1 = {
                'red1': 'Precautions and Carries must be taken at this place in this week.',
                'red2': 'The place has medium temperature. Good weather, but humidity is more.',
                'red3': 'No extra clothing demands. Normal ones would be good. Woah!',
                'red4': 'Temperature is normal. No need to worry.',
                'red5': 'Wear cotton clothes or light woolens.',
                'location': location,
                'temperature': r['main']['temp'],
                'description': r['weather'][0]['description'],
                'icon': r['weather'][0]['icon'],
                'wind_speed': r['wind']['speed'],
                'humidity': r['main']['humidity'],
                'temp_max': r['main']['temp_max'],
                'day_of_cal': datetime.datetime.fromtimestamp(r['dt']).strftime('%A'),
                'date_month_of_cal': datetime.datetime.fromtimestamp(r['dt']).strftime("%d %b"),
            }
        else:
            dict1 = {
                'red1': 'Precautions and Carries must be taken at this place in this week.',
                'red2': 'The place has high temperature. Bad atmosphere may damage skin.',
                'red3': 'Wear cotton clothes. Loose clothes made of linen would be very comfortable.',
                'red4': 'No environment for tourism or sight-seeing.',
                'red5': 'Drink water, even if you don’t feel thirsty. Take a bottle with you always.',
                'location': location,
                'temperature': r['main']['temp'],
                'description': r['weather'][0]['description'],
                'icon': r['weather'][0]['icon'],
                'wind_speed': r['wind']['speed'],
                'humidity': r['main']['humidity'],
                'temp_max': r['main']['temp_max'],
                'day_of_cal': datetime.datetime.fromtimestamp(r['dt']).strftime('%A'),
                'date_month_of_cal': datetime.datetime.fromtimestamp(r['dt']).strftime("%d %b"),
            }
        print(dict1)
    else:
        return redirect('error_404')
    return render(request, 'index.html', dict1)


def error_404(request):
    return render(request, '404.html')
