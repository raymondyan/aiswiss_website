from django.conf.urls import url

from news.views import news, news_detail

urlpatterns = [
    url(r'^(\d+)/$', news, name='news_home'),
    url(r'^(\d+)/(\d+)/$', news_detail, name='news')
]





