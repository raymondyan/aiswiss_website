# Generated by Django 2.0.2 on 2018-02-23 12:34

from django.db import migrations, models
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='school',
            options={'verbose_name': '学校', 'verbose_name_plural': '学校'},
        ),
        migrations.AddField(
            model_name='school',
            name='order',
            field=models.IntegerField(default=0, verbose_name='顺序'),
        ),
        migrations.AlterField(
            model_name='school',
            name='introduce',
            field=froala_editor.fields.FroalaField(verbose_name='简介'),
        ),
    ]
