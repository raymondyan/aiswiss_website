from django.shortcuts import render, render_to_response


# Create your views here.
from hospital.models import Hospital


def show_hospital(request, label):
    assert isinstance(label, str)
    all_hospitals = Hospital.objects.all()
    hospital = Hospital.objects.filter(label__exact=label).first()
    return render_to_response('hospitalAndSchool.html', locals())
