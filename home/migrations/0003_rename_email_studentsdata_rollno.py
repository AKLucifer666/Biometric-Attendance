# Generated by Django 4.2 on 2023-04-07 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_studentsdata_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentsdata',
            old_name='email',
            new_name='rollno',
        ),
    ]
