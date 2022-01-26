from home import views
from django.urls import path 

urlpatterns=[
    path('', views.index, name = 'index'),
    path('question/', views.question, name= 'question'),
    path('about/', views.about, name= 'about'),
    path('question/new_question/', views.new_question, name= 'new_question'),
    path('question/old_question/', views.old_question, name= 'old_question')
]