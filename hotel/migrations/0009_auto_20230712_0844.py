# Generated by Django 3.2.9 on 2023-07-12 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0008_reserve_item_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calender',
            name='day',
            field=models.CharField(default=1, max_length=2),
        ),
        migrations.AlterField(
            model_name='calender',
            name='month',
            field=models.CharField(default=1, max_length=2),
        ),
    ]
