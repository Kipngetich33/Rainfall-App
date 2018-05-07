from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.views.generic import View
from . models import Add_Rainfall
from . methods import list_city_rainfalls,create_labels,assign_colors,assign_borders
from rest_framework.views import APIView
from rest_framework.response import Response
from . forms import RainfallForm, RainfallForm2


User = get_user_model()

class home(View):
    def get(self, request, *args, **kwargs):
        cities_count = Add_Rainfall.objects.all().count()
        chosen_colors = assign_colors(cities_count)
        chosen_borders = assign_borders(cities_count)
        print(chosen_borders)
        return render(request, 'home.html', {"chosen_colors":chosen_colors,"chosen_borders":chosen_borders})



def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data) # http response


class chart(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        all_rainfall = Add_Rainfall.objects.all()
        default_items = list_city_rainfalls(all_rainfall)
        labels = create_labels(all_rainfall)
        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)

def add_rainfall(request):
    '''
    View function that displays a forms that allows users to add a city and rainfall
    '''

    if request.method == 'POST':

        form = RainfallForm2(request.POST ,request.FILES)

        if form.is_valid():
            city = form.cleaned_data['city']
            amount = form.cleaned_data['amount']
            new = Add_Rainfall(amount = amount , city =city)
            new.save()

            return redirect('home')
    else:
        form = RainfallForm2() 
    return render(request, 'add_rainfall.html',{"form" : form})


class timeseries(View):
    def get(self, request, *args, **kwargs):
        cities_count = Add_Rainfall.objects.all().count()
        chosen_colors = assign_colors(cities_count)
        chosen_borders = assign_borders(cities_count)
        return render(request, 'timeseries.html', {"chosen_colors":chosen_colors,"chosen_borders":chosen_borders})


class seriesChart(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        labels = ["January","February","March","April","May","June","July"]
        default_items = []
        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)