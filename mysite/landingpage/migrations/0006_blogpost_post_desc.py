# Generated by Django 3.0.3 on 2020-02-29 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0005_auto_20200229_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='post_desc',
            field=models.TextField(default='', verbose_name='Short description'),
            preserve_default=False,
        ),
    ]
