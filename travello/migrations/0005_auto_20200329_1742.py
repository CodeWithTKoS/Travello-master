# Generated by Django 3.0.4 on 2020-03-29 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0004_auto_20200327_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailed_desc',
            name='dest_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
