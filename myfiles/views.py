from django.shortcuts import render


# Create your views here.
def home(info):
    return render(info, 'index.html')
