# Generated by Django 5.0 on 2024-03-11 05:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminapp', '0002_tbl_warehouse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_warehouse',
            name='warehousereg_district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Adminapp.tbl_district'),
        ),
    ]
