from json import load
from sys import api_version
from django.shortcuts import render
import requests
import os
from dotenv import load_dotenv
load_dotenv()


# Create your views here.
def search(request):
    query = request.GET.get('q')

    if query:
        request.get("https://api.themoviedb.org/3/search/movie?api_key={os.getenv('APIKEY')}&language=en-US&page=1&include_adult=false")


    return render(request, 'search.html')


print(os.getenv('APIKEY'))