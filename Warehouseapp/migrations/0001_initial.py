# Generated by Django 5.0 on 2024-02-19 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_deliveryboy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deliveryboy_name', models.CharField(max_length=50)),
                ('deliveryboy_email', models.CharField(max_length=50)),
                ('deliveryboy_password', models.CharField(max_length=50)),
                ('deliveryboy_address', models.CharField(max_length=50)),
            ],
        ),
    ]