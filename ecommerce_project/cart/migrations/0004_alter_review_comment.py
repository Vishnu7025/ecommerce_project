# Generated by Django 3.2.15 on 2022-09-02 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.TextField(blank=True, max_length=250),
        ),
    ]
