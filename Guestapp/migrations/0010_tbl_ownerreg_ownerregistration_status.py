# Generated by Django 5.0 on 2024-03-11 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guestapp', '0009_tbl_userreg'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_ownerreg',
            name='ownerregistration_status',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
