from django import forms
from .models import UserProfile

# class ProfileForm(forms.Form):
#     user_image = forms.ImageField(label='')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = "__all__"
        labels = {'image': '',}

