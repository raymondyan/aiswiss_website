from django.db import models
from froala_editor.fields import FroalaField


# Create your models here.

class School(models.Model):
    label = models.CharField(max_length=50, verbose_name="标签")
    name = models.CharField(max_length=50, verbose_name="学校名")
    introduce = FroalaField(theme='dark', verbose_name="简介")
    order = models.IntegerField(verbose_name="顺序", default=0)

    def __unicode__(self):
        return self.label

    class Meta:
        verbose_name = "学校"
        verbose_name_plural = "学校"
