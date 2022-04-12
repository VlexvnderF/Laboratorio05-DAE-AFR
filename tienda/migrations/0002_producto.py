# Generated by Django 4.0.4 on 2022-04-12 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6)),
                ('stock', models.IntegerField(default=0)),
                ('pub_date', models.DateField(verbose_name='date published')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.categoria')),
            ],
        ),
    ]
