# Generated by Django 3.0.5 on 2020-08-25 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200825_0302'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='image',
            field=models.ImageField(default=1, upload_to='Service'),
            preserve_default=False,
        ),
    ]
