# Generated by Django 4.2.7 on 2023-12-31 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='account_no',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]
