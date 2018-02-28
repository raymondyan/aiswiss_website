from django.db import models
from froala_editor.fields import FroalaField


# Create your models here.

class News(models.Model):
    NEWS_TYPE = (
        (1, '公司新闻'),
        (2, '行业新闻'),
    )
    title = models.CharField(max_length=30, verbose_name="文章标题", blank=False)
    newsType = models.IntegerField(choices=NEWS_TYPE, verbose_name="文章类型", null=False, blank=False)
    feature = models.FileField(upload_to='./upload/', default=None)
    experts = models.TextField(verbose_name="摘要", default="")
    content = FroalaField(verbose_name="文章内容", blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "新闻"
        verbose_name_plural = "新闻"
