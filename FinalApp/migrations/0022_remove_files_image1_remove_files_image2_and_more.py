# Generated by Django 4.1.4 on 2023-06-23 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinalApp', '0021_remove_files_file_files_image1_files_image2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='files',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='files',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='files',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='files',
            name='image4',
        ),
        migrations.RemoveField(
            model_name='files',
            name='image5',
        ),
        migrations.AddField(
            model_name='files',
            name='file',
            field=models.ImageField(default=2, upload_to='files/'),
            preserve_default=False,
        ),
    ]
