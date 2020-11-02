# Generated by Django 3.1.1 on 2020-10-27 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(db_column='id_producto', primary_key=True, serialize=False)),
                ('numero', models.IntegerField(blank=True, null=True)),
                ('nombre', models.CharField(blank=True, max_length=20, null=True)),
                ('precio', models.IntegerField(blank=True, null=True)),
                ('stock', models.IntegerField(blank=True, null=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='foto')),
                ('tipo', models.CharField(blank=True, max_length=20, null=True)),
                ('activo', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ['numero'],
            },
        ),
    ]
