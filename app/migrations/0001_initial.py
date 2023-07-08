# Generated by Django 4.2.2 on 2023-07-08 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chocolate',
            fields=[
                ('cname', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('flavour', models.CharField(max_length=100)),
                ('cimage', models.ImageField(upload_to=None)),
                ('cost', models.IntegerField()),
                ('description', models.TextField(default='chocolate')),
            ],
        ),
    ]