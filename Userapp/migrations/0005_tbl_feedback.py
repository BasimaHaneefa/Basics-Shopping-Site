# Generated by Django 4.2.7 on 2024-03-16 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Guestapp', '0010_tbl_ownerreg_ownerregistration_status'),
        ('Userapp', '0004_tbl_complaint'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_content', models.CharField(max_length=300)),
                ('feedback_date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guestapp.tbl_userreg')),
            ],
        ),
    ]
