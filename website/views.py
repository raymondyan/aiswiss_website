from django.shortcuts import render_to_response

from news.models import News


def index(request):
    return render_to_response('homepage.html', locals())


def about_us(request):
    return render_to_response('about_us.html', locals())


def education(request):
    return render_to_response('education.html', locals())


def health(request):
    return render_to_response('health.html', locals())


def news(request, news_type):
    if news_type == '0':
        select_news = News.objects.all()
    else:
        select_news = News.objects.filter(newsType__exact=news_type)
    print(select_news)
    return render_to_response('news_home.html', locals())
