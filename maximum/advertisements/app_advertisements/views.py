from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Advertisements
from .forms import AdvertisementForms
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    title=request.GET.get('query')
    print(title)
    if title:
        advertisements=Advertisements.objects.filter(title__icontains=title)
    else:
        advertisements = Advertisements.objects.all()
    context={'advertisements':advertisements,
             'title': title}
    return render(request, 'app_advertisements/index.html', context)


def top_sellers(request):
    users=User.objects.annotate(adv_count=Count('advertisements')).order_by('-adv_count')
    context={'users': users}
    return render(request, 'app_advertisements/top-sellers.html', context)


@login_required(login_url=reverse_lazy('login'))
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
    return render(request, 'app_advertisements/advertisement-post.html', context)


def adv_detail(request, pk):
    advertisements = Advertisements.objects.get(id=pk)
    context = {'advertisements': advertisements}
    return render(request, 'app_advertisements/advertisement.html', context)