# Generated by Django 3.0.4 on 2020-06-14 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0012_wishlist_std'),
        ('tutors', '0011_wishlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='WishList_tut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='students.Student')),
                ('tutors', models.ManyToManyField(blank=True, related_name='tutor_wish', to='tutors.Tutor')),
            ],
        ),
    ]
