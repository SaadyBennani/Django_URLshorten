from django.shortcuts import render
from django.http import HttpResponse
import random
import string
from .models import URL


# Create your views here.
def index(request):
    return render(request, 'url_shorten/index.html')


def shortened(request):
    if request.method == 'POST':
        long_url = request.POST['url']
        short_url = shortify()
        url = URL(url_long=long_url, url_short=short_url)
        url.save()
        return render(request, 'url_shorten/short.html', {'short_url': short_url, 'long_url': url})


def shortify(size=8):
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size))
