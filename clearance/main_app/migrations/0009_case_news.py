# Generated by Django 4.2.2 on 2023-06-20 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_case_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='news',
            field=models.URLField(blank=True, max_length=128),
        ),
    ]
