# Generated by Django 3.2.3 on 2021-06-01 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotto_ussd', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
