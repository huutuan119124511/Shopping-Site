# Generated by Django 3.0.7 on 2020-06-20 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20200602_2151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donhang',
            old_name='cart_origin',
            new_name='cart',
        ),
    ]
