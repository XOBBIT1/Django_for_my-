from django.shortcuts import render
from .models import Image
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'my_app/main_page.html')

def about(request):
    image = Image.objects.order_by('-id')
    return render(request, 'my_app/about.html', {'title': 'Главная страница сайта',
                                                 'image': image})

