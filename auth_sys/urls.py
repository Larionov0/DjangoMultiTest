from django.urls import path
# from django.contrib.auth import views
from . import views

app_name = 'auth_sys'

urlpatterns = [
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_in_handler/', views.sign_in_handler, name='sign_in_handler'),
    path('log_out/', views.log_out, name='log_out'),
    path('sign_up/', views.RegisterFormView.as_view(), name='sign_up'),
]
