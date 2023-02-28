# Generated by Django 3.2 on 2023-02-27 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, unique=True, verbose_name='Enter an alias')),
                ('firstname', models.CharField(max_length=64)),
                ('lastname', models.CharField(max_length=65)),
                ('email', models.EmailField(max_length=65, unique=True)),
            ],
        ),
    ]
