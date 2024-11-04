from django.urls import path
from . import views

urlpatterns = [
    path("create-profile", views.CreateProfileView.as_view(), name="create-profile" )
]