from django.urls import path
from . import views

app_name = 'api_v1'

urlpatterns = [
    path('get_points/', views.get_points, name='get_points'),
    path('new_point/', views.new_point, name='new_point')
]