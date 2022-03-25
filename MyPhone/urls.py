from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('create/', views.PhoneCreateView.as_view(), name='create'),
    path('update/', views.PhoneCreateView.as_view(), name='update'),
]