# Generated by Django 4.1.2 on 2022-10-26 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
