# Generated by Django 2.0.7 on 2018-07-25 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.UUIDField(default=None, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('pwd', models.CharField(max_length=32)),
            ],
        ),
    ]
