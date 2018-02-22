from django.shortcuts import render, render_to_response


# Create your views here.
from school.models import School


def show_school(request, label):
    assert isinstance(label, str)
    all_hospitals = School.objects.all()
    hospital = School.objects.filter(label__exact=label).first()
    print(hospital.introduce)
    return render_to_response('hospitalAndSchool.html', locals())