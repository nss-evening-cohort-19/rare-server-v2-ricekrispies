# Generated by Django 4.1.4 on 2022-12-14 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RareUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('uid', models.CharField(max_length=50)),
                ('bio', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=50)),
                ('created_on', models.DateField()),
                ('active', models.BooleanField()),
                ('is_staff', models.BooleanField()),
                ('profile_image_url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('publication_date', models.DateField()),
                ('content', models.CharField(max_length=250)),
                ('approved', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rareapi.rareuser')),
            ],
        ),
    ]
