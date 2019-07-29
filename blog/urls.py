from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('works/', views.works, name='works'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact')
]
