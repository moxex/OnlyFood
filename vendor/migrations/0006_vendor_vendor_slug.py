# Generated by Django 3.2.7 on 2022-10-02 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0005_rename_user_profile_vendor_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='vendor_slug',
            field=models.SlugField(blank=True, max_length=100),
        ),
    ]