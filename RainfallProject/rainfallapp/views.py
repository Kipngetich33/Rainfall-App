from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from . models import Add_Rainfall

from rest_framework.views import APIView
from rest_framework.response import Response


User = get_user_model()

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html', {"customers": 10})



def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data) # http response


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        # qs_count = User.objects.all().count()
        labels = ["Blue", "Yellow", "Green", "Purple", "Orange"]
        default_items = [23, 2, 3, 12, 2]
        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)

def add_rainfall(request):
    rainfall_object = Add_Rainfall(amount= 4, city = 'Nairobi')
    rainfall_object.save()
    all = Add_Rainfall.objects.all().count()
    print(all)
    return render(request, 'charts.html', {"customers": 10})
