# Generated by Django 2.2.12 on 2021-03-02 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_service_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='blogHaru',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='my blogs')),
            ],
        ),
    ]
