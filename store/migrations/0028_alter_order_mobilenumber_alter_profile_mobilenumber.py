# Generated by Django 4.1.7 on 2023-04-26 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0027_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='mobilenumber',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mobilenumber',
            field=models.IntegerField(),
        ),
    ]
