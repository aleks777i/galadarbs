# Generated by Django 3.2 on 2021-05-06 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deposit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='interest',
            field=models.IntegerField(default=200),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='rate',
            field=models.FloatField(),
        ),
    ]
