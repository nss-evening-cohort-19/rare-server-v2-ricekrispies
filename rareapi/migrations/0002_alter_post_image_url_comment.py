# Generated by Django 4.1.4 on 2022-12-21 01:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rareapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_url',
            field=models.CharField(max_length=1000),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateField()),
                ('content', models.CharField(max_length=250)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rareapi.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rareapi.rareuser')),
            ],
        ),
    ]
