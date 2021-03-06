# Generated by Django 2.0.2 on 2018-02-23 12:41

from django.db import migrations, models
import froala_editor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='文章标题')),
                ('newsType', models.IntegerField(choices=[(1, '公司新闻'), (2, '行业新闻')], verbose_name='文章类型')),
                ('content', froala_editor.fields.FroalaField(verbose_name='文章内容')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '新闻',
                'verbose_name_plural': '新闻',
            },
        ),
    ]
