from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
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

class ThankYouView(TemplateView):
    template_name="reviews/thank_you.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        context['message']="Thank you for your review!"
        return context

'''
class ReviewListView(TemplateView):
    template_name="reviews/reviews_list.html"

    def get_context_data(self, **kwargs):
        context= super().get_context_data()
        reviews=Review.objects.all()
        context['reviews']=reviews
        return context
'''


class ReviewListView(ListView):
    template_name="reviews/reviews_list.html"
    model = Review
    context_object_name = 'reviews'

    # def get_queryset(self):
    #     base_query=super().get_queryset()
    #     data=base_query.filter(rating__gt=4)
    #     return data




class SingleReviewView(TemplateView):
    template_name="reviews/single_review.html"

    def get_context_data(self, **kwargs):
        context= super().get_context_data()
        review_id=kwargs['id']
        selected_review=Review.objects.get(pk=review_id)
        context['review']=selected_review
        return context
