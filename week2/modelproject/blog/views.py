from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs':blogs})

def detail(request, id):
    # blog = Blog.objects.get(id = id)
    blog = get_object_or_404(Blog, pk = id)
    return render(request, 'detail.html', {'blog':blog})