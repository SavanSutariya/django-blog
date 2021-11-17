from django.shortcuts import render
from .models import Post
# Create your views here.
def home(request):
    posts = [
        {
            'title' : 'Post 1',
            'publisher' : 'Savan Sutariya',
            'content' : 'The content of my first blog post',
            'published_date' : 'August 28, 2021'
        },
        {
            'title' : 'Post 2',
            'publisher' : 'Mayur Patel',
            'content' : 'The content of my Second blog post',
            'published_date' : 'August 28, 2021'
        },
        {
            'title' : 'Post 3',
            'publisher' : 'Kishan Modasia',
            'content' : 'The content of my Third blog post',
            'published_date' : 'August 29, 2021'
        }
    ]
    context = {'posts':Post.objects.all()}
    return render(request,'blog/home.html',context)
def about(request):
    return render(request,'blog/about.html',{'title': 'About'})
