# Generated by Django 4.1.7 on 2023-04-01 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake_app', '0004_cake_slug_alter_techcard_model_cake'),
    ]

    operations = [
        migrations.AddField(
            model_name='cake',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
