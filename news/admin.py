from django.contrib import admin

from news.models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "newsType", "created_at")
    search_fields = ('title',)
    list_filter = ('newsType',)


admin.site.register(News, NewsAdmin)
