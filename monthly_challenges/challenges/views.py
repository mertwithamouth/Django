from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
# Create your views here.



monthly_challenges={
    "january":"January is Mary",
    "february":"February is Dairy",
    "march":"March is Dutch",
    "april":"April is Sevil",
    "may":"May is Jay",
    "june":"June is Dune",
    "july":"July is Blury",
    "august":"August is Duty",
    "september":"September is time for Berber",
    "october":"October is time to be Derbeder ",
    "november":"November is time to be in Cember",
    "december":"December is time eat Pastırma's Ceper",
}


def index(request):
    list_items=""
    months=list(monthly_challenges.keys())
    for month in months:
        capitilized_month=month.capitalize()
        month_path=reverse("month-challenge", args=[month]) #/challenge
        list_items += f"""
        <li><a href="{month_path}"> {capitilized_month} </a></li>
        """
    response_data = f"<ol>{list_items}</ol>"
    #return HttpResponse((response_data))
    return render(request, "challenges/challenge.html",
           {"var": response_data})

def monthly_challenge_by_number(request,month):

    months=list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month=months[month-1]
    redirect_path=reverse("month-challenge", args=[redirect_month]) #/challenge
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request,month):
    try:
        challenge_text=monthly_challenges[month]
        return render(request,"challenges/challenge.html",
                      {  "text":challenge_text,
                                "month_name":month})

    except:
        return HttpResponseNotFound("Sorry, that month does not exist.")


