# Generated by Django 3.2.7 on 2022-09-28 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0003_rename_user_profile_vendor_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendor',
            old_name='profile',
            new_name='user_profile',
        ),
    ]
