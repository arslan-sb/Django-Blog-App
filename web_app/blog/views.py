from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
posts=[
    {
        'title': 'Mamu',
        'author':'Arslan',
        'date_posted': datetime.datetime(2020,5,17),
        'content':'This is first post'
    },
    {
        'title': 'Bhanja',
        'author':'Hassan',
        'date_posted': datetime.datetime(2020,4,13),
        'content':'This is  Hassan\'s first post',
    }
]

def home(request):

    return render(request,'blog/home.html',{'posts':posts,'title':'Blogs'})


def about(request):

    return render(request, 'blog/about.html',{'title':'About'})