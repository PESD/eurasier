# Generated by Django 2.1.3 on 2019-01-04 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qsort', '0002_auto_20181119_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='cost',
            field=models.IntegerField(default=1000),
        ),
    ]
