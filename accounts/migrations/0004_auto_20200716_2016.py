# Generated by Django 3.0.6 on 2020-07-16 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200716_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
