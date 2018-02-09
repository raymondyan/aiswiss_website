from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('education', views.index, name='index'),
    path('about', views.about_us, name='index'),
    path('health_care', views.index, name='index'),
    path('news', views.index, name='index')
]