# Generated by Django 3.2 on 2021-05-06 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deposit', models.IntegerField()),
                ('term', models.IntegerField()),
                ('rate', models.IntegerField()),
                ('interest', models.IntegerField()),
            ],
        ),
    ]
