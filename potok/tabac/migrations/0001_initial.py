# Generated by Django 5.1 on 2025-03-02 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tabac',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=30)),
                ('flavor', models.CharField(blank=True, max_length=30, null=True)),
                ('empty', models.BooleanField(default=True)),
            ],
        ),
    ]
