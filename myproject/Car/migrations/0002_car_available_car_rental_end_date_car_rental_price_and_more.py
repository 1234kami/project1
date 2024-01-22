# Generated by Django 5.0 on 2023-12-18 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Car', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='car',
            name='rental_end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='rental_price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='rental_start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='rented_by',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]