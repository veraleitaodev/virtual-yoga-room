# Generated by Django 3.1.6 on 2021-02-16 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210216_1124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='description',
            new_name='summary',
        ),
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]
