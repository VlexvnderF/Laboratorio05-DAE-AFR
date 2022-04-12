# Generated by Django 4.0.4 on 2022-04-12 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('dni', models.IntegerField()),
                ('telef', models.IntegerField()),
                ('direccion', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('fecha_naci', models.DateField(verbose_name='fecha de nacimiento')),
                ('fecha_publi', models.DateTimeField(verbose_name='fecha de publicación')),
            ],
        ),
    ]
