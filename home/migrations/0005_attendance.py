# Generated by Django 4.2 on 2023-04-08 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_studentsdata_photo_coordinates'),
    ]

    operations = [
        migrations.CreateModel(
            name='attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('rollno', models.CharField(max_length=125)),
                ('branch', models.CharField(max_length=125)),
                ('date', models.CharField(max_length=125)),
            ],
        ),
    ]
