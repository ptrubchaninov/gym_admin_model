# Generated by Django 4.1.6 on 2023-02-07 15:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_alter_subscription_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='due_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 7, 15, 59, 33, 357365, tzinfo=datetime.timezone.utc), null=True, verbose_name='Expires'),
        ),
    ]