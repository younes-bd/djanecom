# Generated by Django 3.1.6 on 2021-03-13 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='isAdmin',
            field=models.BooleanField(default=False),
        ),
    ]
