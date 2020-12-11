from django.shortcuts import render_to_response


def index(request):
    tab = "index"
    return render_to_response('homepage.html', locals())


def about_us(request):
    tab = "us"
    return render_to_response('about_us.html', locals())

def show_1(request):
    return render_to_response('1.html', locals())

def show_2(request):
    return render_to_response('2.html', locals())

def show_2s(request):
    return render_to_response('2s.html', locals())

def education(request):
    tab = "edu"
    return render_to_response('education.html', locals())


def health(request):
    tab = "health"
    return render_to_response('health.html', locals())
