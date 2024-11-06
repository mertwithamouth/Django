from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import View
from .forms import ProfileForm
from .models import UserProfile

from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

# Create your views here.


# class CreateProfileView(View):
#     def get(self, request, *args, **kwargs):
#         form = ProfileForm()
#         return render(request, 'profiles/create_profile.html',
#                       {'form': form})
#
#     def post(self, request, *args, **kwargs):
#             submitted_form=ProfileForm(request.POST, request.FILES)
#
#             if submitted_form.is_valid():
#                 profile= UserProfile(image=request.FILES['user_image'])
#                 profile.save()
#                 return HttpResponseRedirect('/profiles/create-profile')
#             return render(request, 'profiles/create_profile.html',
#                           {'form': submitted_form})

class CreateProfileView(CreateView):
    model = UserProfile
    form_class = ProfileForm
    template_name = 'profiles/create_profile.html'
    success_url = '/profiles/create-profile'

class ProfilesView(ListView):
    model = UserProfile
    template_name = 'profiles/user_profiles.html'
    context_object_name = 'profiles'

