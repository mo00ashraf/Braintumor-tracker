# Generated by Django 4.1.4 on 2023-06-23 19:06

import FinalApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinalApp', '0013_delete_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='file',
            field=models.FileField(upload_to=FinalApp.models.rename_uploaded_file),
        ),
    ]