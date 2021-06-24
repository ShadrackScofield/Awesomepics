# Generated by Django 3.1.4 on 2021-02-01 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Picha', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dog_pics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='images/')),
            ],
            options={
                'verbose_name_plural': 'Dogs',
            },
        ),
        migrations.CreateModel(
            name='Tech_pics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='images/')),
            ],
            options={
                'verbose_name_plural': 'Techies',
            },
        ),
    ]
