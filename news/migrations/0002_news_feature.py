# Generated by Django 2.0.2 on 2018-02-23 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='feature',
            field=models.FileField(default=None, upload_to='./media/upload/'),
        ),
    ]
