# Generated by Django 3.0.7 on 2020-06-29 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voucher', '0003_auto_20200627_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voucher',
            name='ngay_bat_dau',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='voucher',
            name='ngay_het_han',
            field=models.DateTimeField(),
        ),
    ]
