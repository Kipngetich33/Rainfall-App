"""RainfallProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from  rainfallapp.views import home, get_data, chart, add_rainfall,timeseries,seriesChart


urlpatterns = [
    url(r'^$', home.as_view(), name='home'),
    url(r'^timeseries/', timeseries.as_view(), name='timeseries'),
    url(r'^api/data/$', get_data, name='api-data'),
    url(r'^rainfall/add', add_rainfall, name='Add-Rainfall'),
    url(r'^api/chart/data/$', chart.as_view()),
    url(r'^api/chart/series/$', seriesChart.as_view()),
    url(r'^admin/', admin.site.urls),

]