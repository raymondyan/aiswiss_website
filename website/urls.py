from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('education', views.education, name='index'),
    path('about', views.about_us, name='about_us'),
    path('health_care', views.health, name='health'),
    path('news', views.index, name='index')
]