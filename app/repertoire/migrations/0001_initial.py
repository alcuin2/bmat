# Generated by Django 3.2.11 on 2022-01-07 18:41

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('filename', models.CharField(max_length=255)),
                ('work_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('proprietary_id', models.IntegerField()),
                ('iswc', models.CharField(max_length=255)),
                ('source', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('contributors', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), size=None)),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='works', to='repertoire.file')),
            ],
        ),
    ]
