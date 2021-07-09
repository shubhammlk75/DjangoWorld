
from django.urls import path
from . import views



urlpatterns = [
    
    path('',views.allblog,name='blog/allblog'),
    path('<int:blog_id>/',views.detail,name='detail'),
    
] 