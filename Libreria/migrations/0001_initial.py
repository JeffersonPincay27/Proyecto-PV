# Generated by Django 4.1.7 on 2023-03-20 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='libro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('imagen', models.ImageField(null=True, upload_to='imaganes/', verbose_name='imagen')),
                ('description', models.TextField(null=True, verbose_name='Descripcion')),
            ],
        ),
    ]
