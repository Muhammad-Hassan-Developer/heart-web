# Generated by Django 3.1.3 on 2024-04-25 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0025_auto_20240425_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='payment_verified',
            field=models.BooleanField(default=False),
        ),
    ]
