# Generated by Django 4.1.4 on 2023-06-23 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinalApp', '0016_alter_files_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='files',
            name='file_save',
        ),
        migrations.AlterField(
            model_name='files',
            name='file',
            field=models.ImageField(upload_to='files/'),
        ),
    ]