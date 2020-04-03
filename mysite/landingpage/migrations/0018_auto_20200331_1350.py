# Generated by Django 3.0.3 on 2020-03-31 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0017_auto_20200307_2116'),
    ]

    operations = [
        migrations.CreateModel(
            name='customTag',
            fields=[
                ('tag', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='blogpost',
            name='custom_tag',
            field=models.ManyToManyField(to='landingpage.customTag'),
        ),
    ]
