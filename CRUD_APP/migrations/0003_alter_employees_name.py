# Generated by Django 4.1.6 on 2023-07-14 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD_APP', '0002_alter_employees_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='name',
            field=models.TextField(max_length=200),
        ),
    ]
