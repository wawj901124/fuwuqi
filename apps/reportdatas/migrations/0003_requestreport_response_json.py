# Generated by Django 2.0.5 on 2019-10-22 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportdatas', '0002_requestreport'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestreport',
            name='response_json',
            field=models.TextField(blank=True, default='', null=True, verbose_name='接口响应json'),
        ),
    ]