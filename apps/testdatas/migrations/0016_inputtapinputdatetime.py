# Generated by Django 2.0.5 on 2019-09-18 15:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testdatas', '0015_auto_20190918_1440'),
    ]

    operations = [
        migrations.CreateModel(
            name='InputTapInputDateTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_ele_find', models.CharField(blank=True, default='xpath', help_text='元素查找风格：id、name、class_name、tag_name、link_text、partial_link_text、css_selector、xpath', max_length=100, null=True, verbose_name='时间输入框查找风格')),
                ('input_ele_find_value', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='时间输入框查找风格的确切值')),
                ('date_ele_find', models.CharField(blank=True, default='xpath', help_text='元素查找风格：id、name、class_name、tag_name、link_text、partial_link_text、css_selector、xpath', max_length=100, null=True, verbose_name='日期元素查找风格')),
                ('date_ele_find_value', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='日期元素查找风格的确切值')),
                ('last_month_ele_find', models.CharField(blank=True, default='xpath', help_text='元素查找风格：id、name、class_name、tag_name、link_text、partial_link_text、css_selector、xpath', max_length=100, null=True, verbose_name='上一月按钮查找风格')),
                ('last_month_ele_find_value', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='上一月按钮查找风格的确切值')),
                ('click_last_month_counts', models.CharField(blank=True, default='', help_text='点击上一月按钮的次数，请填写数字，例如：1、2、3', max_length=100, null=True, verbose_name='点击上一月按钮的次数')),
                ('next_month_ele_find', models.CharField(blank=True, default='xpath', help_text='元素查找风格：id、name、class_name、tag_name、link_text、partial_link_text、css_selector、xpath', max_length=100, null=True, verbose_name='下一月按钮查找风格')),
                ('next_month_ele_find_value', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='下一月按钮查找风格的确切值')),
                ('click_next_month_counts', models.CharField(blank=True, default='', help_text='点击下一月按钮的次数，请填写数字，例如：1、2、3', max_length=100, null=True, verbose_name='点击下一月按钮的次数')),
                ('last_year_ele_find', models.CharField(blank=True, default='xpath', help_text='元素查找风格：id、name、class_name、tag_name、link_text、partial_link_text、css_selector、xpath', max_length=100, null=True, verbose_name='上一年按钮查找风格')),
                ('last_year_ele_find_value', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='上一年按钮查找风格的确切值')),
                ('click_last_year_counts', models.CharField(blank=True, default='', help_text='点击上一年按钮的次数，请填写数字，例如：1、2、3', max_length=100, null=True, verbose_name='点击上一年按钮的次数')),
                ('next_year_ele_find', models.CharField(blank=True, default='xpath', help_text='元素查找风格：id、name、class_name、tag_name、link_text、partial_link_text、css_selector、xpath', max_length=100, null=True, verbose_name='下一年按钮查找风格')),
                ('next_year_ele_find_value', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='下一年按钮查找风格的确切值')),
                ('click_next_year_counts', models.CharField(blank=True, default='', help_text='点击下一年按钮的次数，请填写数字，例如：1、2、3', max_length=100, null=True, verbose_name='点击下一年按钮的次数')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新时间')),
                ('newaddandcheck', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.PROTECT, to='testdatas.NewAddAndCheck', verbose_name='依赖的添加场景')),
            ],
            options={
                'verbose_name': '时间输入框相关内容',
                'verbose_name_plural': '时间输入框相关内容',
            },
        ),
    ]
