# Generated by Django 5.0.6 on 2024-07-01 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=30)),
                ('nroCarnet', models.CharField(max_length=30)),
            ],
        ),
    ]