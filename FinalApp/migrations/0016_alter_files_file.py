# Generated by Django 4.1.4 on 2023-06-23 19:57

import FinalApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinalApp', '0015_files_file_save_alter_files_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='file',
            field=models.ImageField(storage=FinalApp.models.RenameStorage(), upload_to='images/'),
        ),
    ]