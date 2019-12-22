# Generated by Django 2.0.5 on 2019-12-06 11:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reportdatas', '0009_auto_20191115_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='pageloadtimereport',
            name='write_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='用户名'),
        ),
    ]