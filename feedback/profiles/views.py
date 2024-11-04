from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import View
from .forms import ProfileForm
# Create your views here.

def store_file(file):
    with open('temp/image.jpg', 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
class CreateProfileView(View):
    def get(self, request, *args, **kwargs):
        form = ProfileForm()
        return render(request, 'profiles/create_profile.html',
                      {'form': form})

    def post(self, request, *args, **kwargs):
            submitted_form=ProfileForm(request.POST, request.FILES)
            if submitted_form.is_valid():
                store_file(request.FILES['image'])
                return HttpResponseRedirect('/profiles/create-profile')
            return render(request, 'profiles/create_profile.html',
                          {'form': submitted_form})
