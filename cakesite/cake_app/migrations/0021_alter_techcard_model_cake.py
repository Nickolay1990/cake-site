# Generated by Django 4.1.7 on 2023-06-05 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cake_app', '0020_alter_techcard_data_alter_techcard_model_cake'),
    ]

    operations = [
        migrations.AlterField(
            model_name='techcard',
            name='model_cake',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cake_app.cake', verbose_name='Торт'),
        ),
    ]
