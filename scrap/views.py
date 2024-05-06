from django.shortcuts import render,redirect
import requests
from bs4 import BeautifulSoup
from .models import Link
# from django.http import HttpResponseRedirect
# Create your views here.

def scrape(request):
    if request.method=='POST':
        text = request.POST.get('text')
        page = requests.get(text)
        soup = BeautifulSoup(page.text,'html.parser')

        for link in soup.find_all('a'):
            link_address = link.get('href')
            link_text = link.string
            Link.objects.create(name=link_text,address=link_address)
        return redirect('scrape')
    else: 
        data = Link.objects.all()
    return render(request,'result.html',{'data':data})

def delete(request):
    Link.objects.all().delete()
    return render(request,'result.html')