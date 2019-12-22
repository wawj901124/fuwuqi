# Generated by Django 2.0.5 on 2019-10-22 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapidatas', '0002_requestcookies_requestdatas_requestheaders'),
    ]

    operations = [
        migrations.AddField(
            model_name='apirequestdata',
            name='is_auto_get_cookies',
            field=models.BooleanField(default=True, verbose_name='是否自动获取cookies'),
        ),
        migrations.AddField(
            model_name='apirequestdata',
            name='is_use_cache',
            field=models.BooleanField(default=False, verbose_name='是否使用缓存cookies'),
        ),
    ]