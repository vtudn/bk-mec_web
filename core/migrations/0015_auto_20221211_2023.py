# Generated by Django 2.2.14 on 2022-12-11 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_booking_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='address',
            field=models.CharField(default='268 Lý Thường Kiệt, Phường 14, Quận 10, Thành phố Hồ Chí Minh', max_length=500),
            preserve_default=False,
        ),
    ]
