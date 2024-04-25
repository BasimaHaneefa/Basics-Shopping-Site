# Generated by Django 5.0 on 2024-03-11 07:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Businessowner', '0004_delete_tbl_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_photos', models.FileField(upload_to='GallaryDoc/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Businessowner.tbl_product')),
            ],
        ),
    ]
