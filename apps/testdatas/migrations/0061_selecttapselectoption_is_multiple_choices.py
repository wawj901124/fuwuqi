# Generated by Django 2.0.5 on 2019-11-29 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testdatas', '0060_auto_20191128_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='selecttapselectoption',
            name='is_multiple_choices',
            field=models.BooleanField(default=False, verbose_name='是否多选'),
        ),
    ]
