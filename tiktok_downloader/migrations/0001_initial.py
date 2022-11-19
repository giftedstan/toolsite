# Generated by Django 3.1.8 on 2021-12-16 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TiktokRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]