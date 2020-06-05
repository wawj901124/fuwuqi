# Generated by Django 2.0.5 on 2020-01-17 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testupdatadb', '0007_auto_20191205_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='updatedbdata',
            name='depend_case',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.PROTECT, to='testupdatadb.UpdateDbData', verbose_name='依赖的前置用例'),
        ),
    ]