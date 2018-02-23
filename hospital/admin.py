from django.contrib import admin

from hospital.models import Hospital


class HospitalAdmin(admin.ModelAdmin):
    list_display = ("order", "label", "name")


admin.site.register(Hospital, HospitalAdmin)
