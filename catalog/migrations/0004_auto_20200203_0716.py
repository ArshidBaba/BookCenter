# Generated by Django 3.0.2 on 2020-02-03 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20200131_0611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(blank=True, help_text='13 Character ISBN number</a>', max_length=13),
        ),
    ]
