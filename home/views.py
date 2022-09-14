from django.shortcuts import render
import requests

# Create your views here.
def search(request):
    query = request.GET.get('q')

    if query:
        request.get("https://api.themoviedb.org/3/search/movie?api_key=<<api_key>>&language=en-US&page=1&include_adult=false")


    return render(request, 'search.html')