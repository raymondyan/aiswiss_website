from django.shortcuts import render, render_to_response


# Create your views here.
from school.models import School


def show_school(request, label):
    tab = "edu"
    category="school"
    assert isinstance(label, str)
    all_hospitals = School.objects.all().extra(order_by=['order'])
    hospital = School.objects.filter(label__exact=label).first()
    return render_to_response('hospitalAndSchool.html', locals())
