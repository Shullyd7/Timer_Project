# Generated by Django 4.2.2 on 2023-06-29 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Timer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.IntegerField(default=25)),
                ('is_running', models.BooleanField(default=False)),
                ('remaining_time', models.IntegerField(null=True)),
            ],
        ),
    ]
