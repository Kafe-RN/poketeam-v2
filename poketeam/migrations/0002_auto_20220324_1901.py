# Generated by Django 3.1.5 on 2022-03-24 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poketeam', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poketeam',
            old_name='tema_name',
            new_name='name',
        ),
    ]