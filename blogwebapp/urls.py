from django.urls import path
from . import views
from .views import update_issue
#from . import views
urlpatterns = [
    path('', views.home, name = 'blog-home'),
    path('about/', views.about, name = 'blog-about'),
    path('issues/', views.issues, name = 'blog-issues'),
    path('update_issue/<int:issue_id>/', update_issue, name='update_issue'),
]
