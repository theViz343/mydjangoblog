# Generated by Django 3.0.3 on 2020-04-20 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0023_auto_20200420_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='custom_tag',
            field=models.ManyToManyField(to='landingpage.CustomTag'),
        ),
    ]
