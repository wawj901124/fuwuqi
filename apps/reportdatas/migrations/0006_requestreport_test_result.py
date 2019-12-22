# Generated by Django 2.0.5 on 2019-10-23 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportdatas', '0005_requestreport_testpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestreport',
            name='test_result',
            field=models.CharField(blank=True, choices=[('P0', '通过'), ('P1', '失败')], default='', max_length=10, null=True, verbose_name='接口测试结果'),
        ),
    ]