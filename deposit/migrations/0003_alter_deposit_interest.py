# Generated by Django 3.2 on 2021-05-06 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deposit', '0002_auto_20210506_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='interest',
            field=models.FloatField(),
        ),
    ]
