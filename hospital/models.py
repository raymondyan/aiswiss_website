from django.db import models
from froala_editor.fields import FroalaField

# Create your models here.

class Hospital(models.Model):
    label = models.CharField(max_length=50, verbose_name="标签")
    name = models.CharField(max_length=50, verbose_name="医院名")
    introduce = FroalaField(theme='dark')

    def __unicode__(self):
        return self.label