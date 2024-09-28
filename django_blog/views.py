from django.shortcuts import render



posts = [
    {"title": "Post 1", 
    "content": "This is the content of post",
    "author": "John Doe",
    "created_at": "2020-01-01"},
    {"title": "Post 2", 
    "content": "This is the content of post2",
    "author": "Jane Doe",
    "created_at": "2020-01-01"}

]

def home(request):
    context = {
        'posts':posts
    }
    return render(request,'home.html',context,{'title':'Home Page'})

def about(request):
    return render(request,'about.html',{'title':'About Page'})

