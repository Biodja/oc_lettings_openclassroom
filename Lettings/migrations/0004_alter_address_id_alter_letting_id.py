# Generated by Django 4.1.7 on 2023-03-30 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lettings', '0003_auto_20230225_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='letting',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
