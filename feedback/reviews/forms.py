from django import forms
from .models import Review

'''
class ReviewForm(forms.Form):
    user_name = forms.CharField(label='Username', max_length=12,
                                error_messages={'required': 'Username is required.',
                                                'invalid': 'Username must be maximum 12 letters'})
    review_text = forms.CharField(label='Your Review', max_length=1000, widget=forms.Textarea)
    rating = forms.IntegerField(label='Your Rating', min_value=1, max_value=5)
'''

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        labels={'username': 'Your Name', 'review': 'Your Feedback', 'rating': 'Your Rating'}
        error_messages = {'username': {'required': 'Username is required.',
                                       'invalid': 'Username must be maximum 12 letters'
                                       },
                          'review': {'required': 'Review is required.',
                                       'invalid': 'Review must be maximum 1000 letters'
                                       }
                          }
