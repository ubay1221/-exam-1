# Generated by Django 5.1.3 on 2024-12-01 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('igredients', models.TextField()),
                ('price', models.IntegerField()),
                ('type', models.TextField()),
                ('cuisine', models.TextField()),
            ],
        ),
    ]
