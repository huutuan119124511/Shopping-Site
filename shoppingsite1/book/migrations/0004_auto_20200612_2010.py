# Generated by Django 3.0.7 on 2020-06-12 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20200602_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sach',
            name='hinh_anh',
            field=models.ImageField(blank=True, max_length=254, null=True, upload_to='books/2020/6', verbose_name='Ảnh bìa'),
        ),
    ]
