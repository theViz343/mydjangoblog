# Generated by Django 3.0.3 on 2020-02-29 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='post_title',
            field=models.CharField(default='Blog post', max_length=200),
        ),
    ]
