from django.shortcuts import render, get_object_or_404
from .models import Book

# Create your views here.
def index(request):
    books= Book.objects.all()
    return render(request,template_name="book_outlet/index.html",
                  context={"books":books})


def book_detail(request,slug):
    book = get_object_or_404(Book,title=slug)
    return render(request,template_name="book_outlet/book_detail.html",
                  context={"book":book})