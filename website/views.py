from django.shortcuts import render_to_response


def index(request):
    tab = "index"
    return render_to_response('homepage.html', locals())


def about_us(request):
    tab = "us"
    return render_to_response('about_us.html', locals())


def education(request):
    tab = "edu"
    return render_to_response('education.html', locals())


def health(request):
    tab = "health"
    return render_to_response('health.html', locals())
