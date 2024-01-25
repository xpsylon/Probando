# Generated by Django 4.2.6 on 2024-01-25 10:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pruebas', '0011_buyer_buyerproduct_product_buyerproduct_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
