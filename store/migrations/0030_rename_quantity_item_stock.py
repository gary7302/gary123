# Generated by Django 4.1.7 on 2023-04-26 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0029_item_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='quantity',
            new_name='stock',
        ),
    ]
