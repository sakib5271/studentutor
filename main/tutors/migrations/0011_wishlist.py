# Generated by Django 3.0.4 on 2020-06-13 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0011_auto_20200613_1840'),
        ('tutors', '0010_postanad_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('students', models.ManyToManyField(blank=True, related_name='wishlist_students', to='students.Student')),
                ('tutor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tutors.Tutor')),
            ],
        ),
    ]
