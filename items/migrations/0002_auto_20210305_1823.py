# Generated by Django 3.1.6 on 2021-03-05 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='program',
            old_name='category_friendly_name',
            new_name='category',
        ),
        migrations.RemoveField(
            model_name='program',
            name='category_name',
        ),
    ]