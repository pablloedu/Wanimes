from django.shortcuts import render
import api

# Create your views here.
def index(request):
    return render(request, 'home/newindex.html', 
    {
        'animes': api.animes
    
    }
)
