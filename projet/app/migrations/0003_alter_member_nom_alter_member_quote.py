# Generated by Django 4.2.1 on 2023-06-13 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_membre_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='nom',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='quote',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
