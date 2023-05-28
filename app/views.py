
from django.shortcuts import render,redirect
from bs4 import BeautifulSoup
import requests

# Create your views here.



def via(request):
    if request.method == 'POST':
        bar = request.POST.get('bar')
        type_city = request.POST.get('city')
        return redirect(f'table/{bar}/{type_city}/')
    return render(request,'app/main.html')


def show_info(request,type_city,city):
    url = f'https://ua.sinoptik.ua/погода-{type_city}/2023-05-27'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')

    mini = soup.find('div', {'class': 'min'})
    max = soup.find('div', {'class': 'max'})

    context = {
        'city':city,
        'type_city':type_city,
        'min_temp': mini.text.strip(),
        'max_temp': max.text.strip(),
    }

    return render(request, 'app/info.html', context)







# def main(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         years = request.POST.get('years')
#         series = request.POST.get('series')
#         speed = request.POST.get('speed')
#         price = request.POST.get('price')
#         type_car = request.POST.get('type')
#         return redirect(f'table/{name}/{years}/{series}/{speed}/{price}/{type_car}/')
#     return render(request,'app1/main.html')


# def enter(request,name,years,series,speed,price,type_car):
#     context = {
#         'name':name,
#         'type_car':type_car,
#         'years':years,
#         'series':series,
#         'speed':speed,
#         'price':price
#     }
#     return render(request,'app1/car_page.html',context)

# Иван Проценко, [27.05.2023 21:38]
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',main),
#     path('table/<str:name>/<int:years>/<str:series>/<int:speed>/<int:price>/<str:type_car>/',enter)
# ]
