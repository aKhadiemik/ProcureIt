from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
import os, time

def hello(request):
    return(HttpResponse("Hello World!"))
