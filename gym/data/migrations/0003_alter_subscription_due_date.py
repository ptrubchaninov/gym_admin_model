# Generated by Django 4.1.6 on 2023-02-07 15:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_alter_address_options_alter_customer_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='due_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 7, 15, 59, 26, 444046, tzinfo=datetime.timezone.utc), null=True, verbose_name='Expires'),
        ),
    ]
