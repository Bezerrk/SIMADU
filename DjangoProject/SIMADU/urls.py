from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('mapa/', views.map_view, name='map'),
    path('ocurrences/', views.ocurrences_view, name='ocurrences'),
    path('alerts/', views.alerts_view, name='alerts'),
    path('reports/', views.reports_view, name='reports'),
]
