from django.shortcuts import render
from .models import Post
#from models import Post


#from django.http import HttpResponse 

posts = [
            {
                'author': 'Ian Nyingi' , 
                    'title': 'Surviving is Winning Franklin',
                    'content': 'First Post ',
                    'date_posted': 'July 31 2024'
            },
            {
                'author': 'Maria Jacobs' ,
                'title': 'Pawn lives matter',
                'content': 'Second Post',
                'date_posted': 'August 5 ,2024'
            }

        ]

  
# Create your views here.
def home(request):
    context = {
                'posts': Post.objects.all()
         }
    return render(request, 'blogwebapp/home.html', context)
    #return HttpResponse('<h1> Blog Home </h1>')
    # return HttpResponse('<doctype>>..>')

def about(request):
     return render(request, 'blogwebapp/about.html', {'title': 'About'})


