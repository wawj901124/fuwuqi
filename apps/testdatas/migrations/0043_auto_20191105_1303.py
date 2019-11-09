# Generated by Django 2.0.5 on 2019-11-05 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testdatas', '0042_newaddandcheck_click_confirm_delay_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputtapinputtext',
            name='auto_input_type',
            field=models.CharField(blank=True, choices=[('1', '数字'), ('2', '字母（小写）'), ('3', '字母（大写）'), ('4', '特殊符号'), ('5', '数字和字母（小写）'), ('6', '数字和字母（大写）'), ('7', '字母（大小写）'), ('8', '数字和字母（大小写）'), ('9', '数字和字母和特殊符号'), ('10', '数字和字母和特殊符号和空白字符'), ('11', '汉字'), ('12', '手机号'), ('13', '身份证号')], default='11', max_length=10, null=True, verbose_name='自动输入字符的类型'),
        ),
    ]
