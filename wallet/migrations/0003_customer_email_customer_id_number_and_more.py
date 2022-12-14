# Generated by Django 4.0.6 on 2022-08-01 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0002_delete_account_delete_card_delete_loan_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='id_number',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='nationality',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='occupation',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='pin',
            field=models.SmallIntegerField(max_length=8, null=True),
        ),
    ]
