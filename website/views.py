from django.shortcuts import render_to_response


def index(request):
    return render_to_response('homepage.html', locals())


def about_us(request):
    return render_to_response('about_us.html', locals())