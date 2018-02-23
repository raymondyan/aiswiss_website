from django.db import models
from froala_editor.fields import FroalaField


# Create your models here.

class Hospital(models.Model):
    label = models.CharField(max_length=50, verbose_name="标签")
    name = models.CharField(max_length=50, verbose_name="医院名")
    introduce = FroalaField(theme='dark')
    order = models.IntegerField(verbose_name="顺序", default=0)

    def __unicode__(self):
        return self.label

    class Meta:
        verbose_name = "医院"
        verbose_name_plural = "医院"
