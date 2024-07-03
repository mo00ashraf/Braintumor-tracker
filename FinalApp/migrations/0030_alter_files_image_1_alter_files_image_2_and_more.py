# Generated by Django 4.1.4 on 2023-06-24 12:00

import FinalApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinalApp', '0029_alter_files_image_1_alter_files_image_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='image_1',
            field=models.ImageField(default='', storage=FinalApp.models.RenameStorage(), upload_to=''),
        ),
        migrations.AlterField(
            model_name='files',
            name='image_2',
            field=models.ImageField(default='', storage=FinalApp.models.RenameStorage1(), upload_to=''),
        ),
        migrations.AlterField(
            model_name='files',
            name='image_3',
            field=models.ImageField(default='', storage=FinalApp.models.RenameStorage2(), upload_to=''),
        ),
        migrations.AlterField(
            model_name='files',
            name='image_4',
            field=models.ImageField(default='', storage=FinalApp.models.RenameStorage3(), upload_to=''),
        ),
        migrations.AlterField(
            model_name='files',
            name='image_5',
            field=models.ImageField(default='', storage=FinalApp.models.RenameStorage4(), upload_to=''),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(storage=FinalApp.models.RenameStorag(), upload_to=''),
        ),
        migrations.AlterField(
            model_name='results',
            name='content',
            field=models.ImageField(upload_to=''),
        ),
    ]
