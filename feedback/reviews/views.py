from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from .forms import ReviewForm
from .models import Review
class ReviewView(View):
    def get(self, request, *args, **kwargs):
        form = ReviewForm()
        return render(request, 'reviews/review.html',
                      {'form': form})
    def post(self, request, *args, **kwargs):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thank-you')
        return render(request, 'reviews/review.html',
                      {'form': form})
'''
def review(request):
    if request.method == 'POST':

        form=ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")
    else:
        form=ReviewForm()

    return render(request, 'reviews/review.html',
                           {'form':form})

'''
# Create your views here.

def thank_you(request):
    return render(request, "reviews/thank_you.html")