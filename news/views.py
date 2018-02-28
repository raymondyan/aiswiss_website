from django.shortcuts import render_to_response

from aiswiss_web.settings import MEDIA_URL
from news.models import News


def news(request, news_type):
    tab = "news"
    media_url = MEDIA_URL
    if news_type == '0':
        select_news = News.objects.all()
    else:
        select_news = News.objects.filter(newsType__exact=news_type)
    return render_to_response('news_home.html', locals())


def news_detail(request, news_type, news_id):
    tab = "news"
    detail = News.objects.filter(id=news_id).first()
    return render_to_response('news.html', locals())
