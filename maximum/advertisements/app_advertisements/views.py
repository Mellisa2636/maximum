from django.http import HttpResponse
from django.shortcuts import render
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
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            new_advertisement = form.save(commit=False)
            new_advertisement.user = request.user
            new_advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'app_advertisements/advertisement-post.html', context)


