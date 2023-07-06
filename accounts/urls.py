from django.urls import path
from . import views


urlpatterns = [
    path('sign_up/', views.sign_up, name='sign_up'),
    path('profile/', views.profile, name='profile'),
]