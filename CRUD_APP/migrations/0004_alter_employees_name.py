# Generated by Django 4.1.6 on 2023-07-14 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD_APP', '0003_alter_employees_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
