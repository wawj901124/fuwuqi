# Generated by Django 2.0.5 on 2019-10-22 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportdatas', '0003_requestreport_response_json'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestreport',
            name='response_elapsed_microseconds',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='接口响应elapsed_microseconds(单位：毫秒)'),
        ),
    ]