# Generated by Django 2.2.7 on 2021-01-13 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topping1', models.CharField(max_length=100)),
                ('topping2', models.CharField(max_length=100)),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzaApp.Size')),
            ],
        ),
    ]
