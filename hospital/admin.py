from django.contrib import admin

from hospital.models import Hospital


class HospitalAdmin(admin.ModelAdmin):
    list_display = ("label", "name")


admin.site.register(Hospital, HospitalAdmin)
