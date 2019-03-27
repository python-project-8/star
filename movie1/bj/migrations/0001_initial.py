# Generated by Django 2.0.6 on 2019-03-26 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='catEye_db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=30)),
                ('adress_name', models.CharField(max_length=20)),
                ('wan_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='nuoMi_db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=30)),
                ('adress_name', models.CharField(max_length=100)),
                ('wan_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='taopp_db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=30)),
                ('adress_name', models.CharField(max_length=20)),
                ('wan_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=10)),
                ('u_password', models.CharField(max_length=255)),
                ('u_ticket', models.CharField(max_length=30, null=True)),
            ],
            options={
                'db_table': 'bjw_user',
            },
        ),
    ]
