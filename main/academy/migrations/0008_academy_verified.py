# Generated by Django 3.0.4 on 2020-09-14 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0007_remove_postanad_tuition_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='academy',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
