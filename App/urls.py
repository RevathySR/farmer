from django.urls import path
from . import views 
# from django.conf.urls import url

urlpatterns = [
    
    path('',views.homepage,name = "homepage"),
    path('register/', views.register,name='register' ),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('checkLogin/', views.checkLogin, name = "checkLogin"),
    path('checkSignup/', views.checkSignup,name = 'checkSignup'),
    path('cropPrediction/', views.cropPrediction, name = "cropPrediction"),
    path('sendMsg/', views.sendMsg, name='sendMsg'),
    path('chatsDisplay/', views.chatsDisplay, name='chatsDisplay'),
    path('services/', views.services, name='services'),
    path('blog/<int:pk>', views.blogs, name='blog'),
    path('comment/', views.comments, name='comment'),
    path('createPost/', views.createPost, name='createPost'),
    path('createProduct/', views.createProduct, name='createProduct'),
    path('products/', views.products, name='products'),
    path('ads/', views.ads, name='ads'),
]