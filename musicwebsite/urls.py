
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('calm',views.calm,name='calm'),
    path('happy',views.happy,name='happy'),
    path('sad',views.sad,name='sad'),
    path('party',views.party,name='party'),
    path('angry',views.angry,name='angry'),
    
]
