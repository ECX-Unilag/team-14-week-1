# Generated by Django 3.1 on 2020-08-08 15:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name of clothes')),
                ('slug', models.SlugField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('category', models.CharField(choices=[('CLOTHINGS', 'Clothings'), ('BAGS', 'Bags'), ('SPORTS', 'Sport'), ('SHOES', 'Shoes'), ('ACCESSORIES', 'Accesories')], max_length=15, verbose_name='Category')),
                ('number', models.PositiveIntegerField(verbose_name='Available number')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
