# Generated by Django 4.1.4 on 2023-06-17 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinalApp', '0005_images_mymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultipleImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='mymodel',
            name='images',
        ),
        migrations.DeleteModel(
            name='ImageS',
        ),
        migrations.DeleteModel(
            name='MyModel',
        ),
    ]
