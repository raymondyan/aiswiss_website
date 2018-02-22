from django.contrib import admin

from school.models import School


class SchoolAdmin(admin.ModelAdmin):
    list_display = ("label", "name")


admin.site.register(School, SchoolAdmin)
