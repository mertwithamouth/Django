from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def font(text):
    html_content = f'''
        <html>
            <head>
                <style>
                    p {{
                        font-family: Arial, sans-serif;
                        font-size: 25 px;
                        color: #f32b00;
                    }}

                    h1 {{
                        font-family: Calibri, sans-serif;
                        font-size: 33px;
                        color: #333;
                    }}
                </style>
            </head>
            <body>
                <h1>Merhaba, Django!</h1>
                <p>{text}</p>
            </body>
        </html>
        '''
    return html_content


def index(request):
    return HttpResponse(font("Hello, world. You're at the polls index."))



def monthly_challenges(request,month):
    if month == "january":
        return HttpResponse(font("January is Mary"))
    elif month == "february":
        return HttpResponse(font("February is Daily"))
    elif month == "march":
        return HttpResponse(font("March is Dutch"))
    elif month == "april":
        return HttpResponse(font("April is Sevil"))


