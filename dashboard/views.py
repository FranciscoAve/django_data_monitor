from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.conf import settings

# Create your views here.
def index(request):

    response = requests.get(settings.API_URL)
    posts = response.json()

    total_responses = len(posts)

    data = {
        "title": "Landing Page' Dashboard",
        "total_responses": total_responses
    }
    #return HttpResponse("¡Bienvenido a la aplicación Django!")
    return render(request, 'dashboard/index.html', data)