# Generated by Django 2.0.5 on 2019-09-18 14:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testdatas', '0013_auto_20190918_0920'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssertTipText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tip_ele_find', models.CharField(blank=True, default='xpath', help_text='元素查找风格：id、name、class_name、tag_name、link_text、partial_link_text、css_selector、xpath', max_length=100, null=True, verbose_name='验证元素查找风格')),
                ('tip_ele_find_value', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='验证元素查找风格的确切值')),
                ('tip_text', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='验证元素文本信息内容')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '验证元素相关内容',
                'verbose_name_plural': '验证元素相关内容',
            },
        ),
        migrations.AddField(
            model_name='newaddandcheck',
            name='is_submit_success',
            field=models.BooleanField(default=True, verbose_name='是否添加成功'),
        ),
        migrations.AddField(
            model_name='asserttiptext',
            name='newaddandcheck',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.PROTECT, to='testdatas.NewAddAndCheck', verbose_name='依赖的添加场景'),
        ),
    ]
