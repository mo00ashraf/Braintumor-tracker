# Generated by Django 4.1.4 on 2023-06-25 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinalApp', '0040_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='username',
            field=models.CharField(default=2, max_length=150),
            preserve_default=False,
        ),
    ]