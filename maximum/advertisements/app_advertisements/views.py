from django.http import HttpResponse
from django.shortcuts import render
from .models import Advertisements

# Create your views here.

def index(request):
    advertesements = Advertisements.objects.all()
    context = { 'advertisements' : advertesements}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')