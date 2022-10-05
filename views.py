from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index (request):
    context = {
        'name' : 'Peter',
        'age' : 34,
        'nationality' : 'British',
    }
    return render(request,'index.html')