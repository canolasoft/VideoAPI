# Generated by Django 3.1.7 on 2021-05-27 03:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0007_auto_20210505_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='datapp',
            name='iconapp',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
    ]