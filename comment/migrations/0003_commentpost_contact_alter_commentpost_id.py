# Generated by Django 4.0 on 2023-11-30 02:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('print', '0001_initial'),
        ('comment', '0002_alter_commentpost_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentpost',
            name='contact',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='print.paintpost', verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='commentpost',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]