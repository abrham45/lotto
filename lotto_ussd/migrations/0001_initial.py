from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = [
    ]
    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.TextField(max_length=15)),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('lot_type', models.CharField(max_length=200)),
                ('lot_num', models.TextField(max_length=200)),
            ],
        ),
    ]
