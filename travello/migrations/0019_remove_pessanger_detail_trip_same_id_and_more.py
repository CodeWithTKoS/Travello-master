# Generated by Django 4.2.4 on 2023-10-31 14:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0018_alter_transactions_date_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessanger_detail',
            name='Trip_same_id',
        ),
        migrations.AlterField(
            model_name='transactions',
            name='Date_Time',
            field=models.CharField(default=datetime.datetime(2023, 10, 31, 14, 12, 54, 638961, tzinfo=datetime.timezone.utc), max_length=19),
        ),
    ]
