# Generated by Django 4.2.5 on 2023-10-02 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.FloatField(default=0.0)),
                ('shop', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='shops.shop')),
            ],
        ),
    ]
