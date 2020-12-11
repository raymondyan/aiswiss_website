from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('education', views.education, name='education'),
    path('about', views.about_us, name='about_us'),
    path('health_care', views.health, name='health'),
    path('show_1', views.show_1, name='show_1'),
    path('show_2', views.show_2, name='show_2'),
    path('show_2s', views.show_2s, name='show_2s'),
]
