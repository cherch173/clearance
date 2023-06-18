# Generated by Django 4.2.2 on 2023-06-17 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_case_description_reporting'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reporting',
            options={'ordering': ['-date']},
        ),
        migrations.RemoveField(
            model_name='case',
            name='declassified',
        ),
        migrations.AlterField(
            model_name='case',
            name='description',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='reporting',
            name='date',
            field=models.DateField(verbose_name='Date Published'),
        ),
    ]
