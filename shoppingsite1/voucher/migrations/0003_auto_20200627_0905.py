# Generated by Django 3.0.7 on 2020-06-27 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voucher', '0002_remove_voucher_loai_voucher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voucher',
            name='anh_minh_hoa',
        ),
        migrations.AddField(
            model_name='voucher',
            name='image',
            field=models.ImageField(null=True, upload_to='vouchers/2020/6'),
        ),
    ]
