# Generated by Django 4.0 on 2022-01-01 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood_donation_system_app', '0003_rename_blood_bank_name_donor_blood_bank_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pharmacy',
            name='id',
            field=models.BigAutoField(auto_created=True, default='1', primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='security_guard',
            name='id',
            field=models.BigAutoField(auto_created=True, default='1', primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pharmacy',
            name='Name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='security_guard',
            name='CNIC',
            field=models.CharField(max_length=50),
        ),
    ]
