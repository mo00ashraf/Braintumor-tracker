# Generated by Django 4.1.4 on 2023-06-23 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinalApp', '0020_remove_files_file1_remove_files_file2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='files',
            name='file',
        ),
        migrations.AddField(
            model_name='files',
            name='image1',
            field=models.ImageField(default='', upload_to='files/', verbose_name='Image 1'),
        ),
        migrations.AddField(
            model_name='files',
            name='image2',
            field=models.ImageField(default='', upload_to='files/', verbose_name='Image 2'),
        ),
        migrations.AddField(
            model_name='files',
            name='image3',
            field=models.ImageField(default='', upload_to='files/', verbose_name='Image 3'),
        ),
        migrations.AddField(
            model_name='files',
            name='image4',
            field=models.ImageField(default='', upload_to='files/', verbose_name='Image 4'),
        ),
        migrations.AddField(
            model_name='files',
            name='image5',
            field=models.ImageField(default='', upload_to='files/', verbose_name='Image 5'),
        ),
    ]