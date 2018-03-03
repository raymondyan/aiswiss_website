from django.shortcuts import render, render_to_response

from hospital.models import Hospital


def show_hospital(request, label):
    tab = "health"
    category = "hospital"
    category_cn = "医院"
    assert isinstance(label, str)
    all_hospitals = Hospital.objects.all().extra(order_by=['order'])
    hospital = Hospital.objects.filter(label__exact=label).first()
    return render_to_response('hospitalAndSchool.html', locals())
