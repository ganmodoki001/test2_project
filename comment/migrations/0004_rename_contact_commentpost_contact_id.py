# Generated by Django 4.0 on 2023-11-30 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_commentpost_contact_alter_commentpost_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentpost',
            old_name='contact',
            new_name='contact_id',
        ),
    ]
