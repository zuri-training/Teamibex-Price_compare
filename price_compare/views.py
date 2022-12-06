import re
from unicodedata import name
# from django.http import HttpResponse
from django.shortcuts import render


# def home_view(request):


#     name = "Ayobanjo"
#     HTML_STRING = f"""
# <h1> Hello {name}</h1>
# <p>Testing URL connections</p>
# """
#     return HttpResponse(HTML_STRING)
def homepage(request):
    return render(request, "index.html")
