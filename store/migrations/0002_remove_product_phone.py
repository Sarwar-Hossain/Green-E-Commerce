# Generated by Django 3.1.6 on 2021-03-20 03:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='phone',
        ),
    ]
