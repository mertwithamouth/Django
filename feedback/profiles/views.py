from django.shortcuts import render
from django.views.generic.edit import View
# Create your views here.


class CreateProfileView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'profiles/create_profile.html')

    def post(self, request, *args, **kwargs):
            pass