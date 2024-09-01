from django.urls import path
from . import views

urlpatterns = [
    path("index",views.index),
    path("<month>",views.monthly_challenges),



]