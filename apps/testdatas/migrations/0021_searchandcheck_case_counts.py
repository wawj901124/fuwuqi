# Generated by Django 2.0.5 on 2019-09-19 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testdatas', '0020_auto_20190919_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchandcheck',
            name='case_counts',
            field=models.IntegerField(default='1', help_text='循环次数，请填写数字，例如：1、2、3', verbose_name='循环次数'),
        ),
    ]
