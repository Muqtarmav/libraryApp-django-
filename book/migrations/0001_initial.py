# Generated by Django 4.0.1 on 2022-04-06 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('pageCount', models.IntegerField()),
            ],
        ),
    ]
