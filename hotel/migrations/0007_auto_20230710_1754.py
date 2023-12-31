# Generated by Django 3.2.9 on 2023-07-10 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('hotel', '0006_auto_20230710_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserve_item',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reserve_item', to='hotel.room'),
        ),
        migrations.AlterField(
            model_name='reserve_item',
            name='staying_time',
            field=models.ManyToManyField(related_name='reserve_item', to='hotel.calender'),
        ),
        migrations.CreateModel(
            name='Reserves',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Reserves', to='accounts.guest')),
                ('reserve_item', models.ManyToManyField(related_name='Reserves', to='hotel.reserve_item')),
            ],
        ),
    ]
