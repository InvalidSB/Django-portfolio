# Generated by Django 2.2.12 on 2021-03-30 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_blogharu_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogharu',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
