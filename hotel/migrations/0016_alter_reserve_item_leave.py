# Generated by Django 3.2.9 on 2023-07-13 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0015_reserve_item_leave'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserve_item',
            name='leave',
            field=models.BooleanField(default=False),
        ),
    ]