# Generated by Django 3.2.22 on 2023-10-30 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(default='enter description here'),
            preserve_default=False,
        ),
    ]
