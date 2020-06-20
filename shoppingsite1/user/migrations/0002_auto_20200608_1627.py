# Generated by Django 3.0.6 on 2020-06-08 09:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='diachikhachhang',
            name='id',
            field=models.BigIntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='diachikhachhang',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
