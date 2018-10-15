# Generated by Django 2.1.2 on 2018-10-14 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='kasutajad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('kasutajanimi', models.CharField(max_length=50, unique=True)),
                ('parool', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='raamatud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pealkiri', models.CharField(max_length=50)),
                ('autor', models.CharField(max_length=30)),
                ('kirjastus', models.CharField(max_length=30)),
                ('keel', models.CharField(max_length=10)),
            ],
        ),
    ]