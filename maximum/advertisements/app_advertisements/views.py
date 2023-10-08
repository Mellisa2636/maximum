from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Advertisements
from .forms import AdvertisementForms
from django.urls import reverse

# Create your views here.

def index(request):
    advertesements = Advertisements.objects.all()
    context = { 'advertisements' : advertesements}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')



def adv_post(request):
    form = AdvertisementForms()  
    if request.method == 'POST':
        form = AdvertisementForms(request.POST, request.FILES)  
        if form.is_valid():  
            advertisement = form.save(commit=False)  
            advertisement.user=request.user
            advertisement.save()
            url = reverse('main_page')  
            return redirect(url)  
        else:
            form = AdvertisementForms()
    context = {'form': form}
    return render(request, 'advertisement-post.html', context)