# Generated by Django 4.1.4 on 2023-06-24 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinalApp', '0030_alter_files_image_1_alter_files_image_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='content',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
