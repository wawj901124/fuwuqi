# Generated by Django 2.0.5 on 2019-10-23 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportdatas', '0004_auto_20191022_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestreport',
            name='testpage',
            field=models.CharField(default='', max_length=100, verbose_name='测试页面'),
        ),
    ]
