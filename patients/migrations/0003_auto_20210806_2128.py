# Generated by Django 3.1.7 on 2021-08-06 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_auto_20210806_2100'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patients',
            old_name='Age',
            new_name='age',
        ),
        migrations.AlterField(
            model_name='patients',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]