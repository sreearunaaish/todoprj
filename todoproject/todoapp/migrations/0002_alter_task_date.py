# Generated by Django 3.2.14 on 2022-07-26 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(),
        ),
    ]
