# Generated by Django 4.2.6 on 2024-01-25 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pruebas', '0012_buyer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='buyer',
            name='name',
        ),
    ]
