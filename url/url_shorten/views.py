from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'url_shorten/index.html')


def shortened(request):
    # long_url = request.POST.get['url']
    return render(request, 'url_shorten/short.html')
