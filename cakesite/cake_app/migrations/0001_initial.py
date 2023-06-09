# Generated by Django 4.1.7 on 2023-03-30 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='TechCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cake', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cake_app.cake')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cake_app.product')),
            ],
        ),
    ]
