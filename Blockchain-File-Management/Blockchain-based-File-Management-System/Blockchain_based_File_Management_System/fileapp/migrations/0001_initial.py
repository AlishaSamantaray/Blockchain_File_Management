# Generated by Django 5.1.7 on 2025-03-15 06:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
                ('file_hash', models.CharField(max_length=64)),
                ('previous_hash', models.CharField(max_length=64)),
                ('nonce', models.IntegerField()),
                ('data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/')),
                ('file_hash', models.CharField(max_length=64, unique=True)),
            ],
        ),
    ]
