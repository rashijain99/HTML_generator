from django.shortcuts import render

from .models import Post
from .forms import postForm

def index(request):
    form=postForm()
    return render(request,'index.html',{'form':form})