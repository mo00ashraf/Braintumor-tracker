# Generated by Django 4.0.4 on 2023-07-04 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FinalApp', '0045_remove_files_image_5_files_image_2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='name',
            new_name='firstname',
        ),
    ]