# Generated by Django 3.1.7 on 2021-02-24 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=112)),
                ('email', models.CharField(max_length=112)),
                ('phone', models.CharField(max_length=112)),
                ('message', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]