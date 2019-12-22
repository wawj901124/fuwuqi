# Generated by Django 2.0.5 on 2019-11-28 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testdatas', '0059_auto_20191128_1312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loginandcheck',
            name='code_image_ele_find',
        ),
        migrations.RemoveField(
            model_name='loginandcheck',
            name='code_image_ele_find_value',
        ),
        migrations.AddField(
            model_name='loginandcheck',
            name='code_image_xpath',
            field=models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='验证码xpath路径'),
        ),
        migrations.AddField(
            model_name='loginandcheck',
            name='code_type',
            field=models.CharField(blank=True, default='n4', help_text='验证码类型：n4(4位纯数字)、n5(5位纯数字)、n6（6位纯数字）、e4（4位纯英文）、e5（5位纯英文）、e6（6位纯英文）、ne4（4位英文数字）、ne5（5位英文数字）、ne6（6位英文数字)', max_length=10, null=True, verbose_name='验证码类型'),
        ),
    ]