# Generated by Django 4.2.20 on 2025-04-17 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_studentprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursetitle',
            name='content',
            field=models.TextField(default='Course content'),
        ),
        migrations.AlterField(
            model_name='coursetitle',
            name='details',
            field=models.TextField(default='Course details'),
        ),
    ]
