# Generated by Django 2.1.15 on 2020-04-18 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20200418_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='note',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
