# Generated by Django 4.1.7 on 2023-06-07 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cake_app', '0022_cake_data_delete_techcard'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cake',
            old_name='data',
            new_name='techcard',
        ),
    ]
