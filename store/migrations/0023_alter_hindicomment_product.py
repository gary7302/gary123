# Generated by Django 4.1.7 on 2023-04-18 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_delete_chinesecomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hindicomment',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hindicomment', to='store.hindicategory'),
        ),
    ]
