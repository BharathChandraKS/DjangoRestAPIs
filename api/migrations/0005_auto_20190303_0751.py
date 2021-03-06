# Generated by Django 2.1.7 on 2019-03-03 07:51

import api.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20190302_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='friend_index',
        ),
        migrations.RemoveField(
            model_name='friend',
            name='people_index',
        ),
        migrations.RenameField(
            model_name='people',
            old_name='eye_color',
            new_name='eyeColor',
        ),
        migrations.RemoveField(
            model_name='people',
            name='favourite_food',
        ),
        migrations.RemoveField(
            model_name='people',
            name='favourite_fruit',
        ),
        migrations.RemoveField(
            model_name='people',
            name='favourite_vegetable',
        ),
        migrations.AddField(
            model_name='people',
            name='favourite_fruits',
            field=api.models.ListField(blank=True, null=True, token=','),
        ),
        migrations.AddField(
            model_name='people',
            name='favourite_vegetables',
            field=api.models.ListField(blank=True, null=True, token=','),
        ),
        migrations.AddField(
            model_name='people',
            name='friends',
            field=models.ManyToManyField(blank=True, null=True, related_name='_people_friends_+', to='api.People'),
        ),
        migrations.AlterField(
            model_name='people',
            name='_id',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='balance',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='api.Company'),
        ),
        migrations.AlterField(
            model_name='people',
            name='email',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='guid',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='has_died',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='index',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='people',
            name='tags',
            field=api.models.ListField(blank=True, null=True, token=','),
        ),
        migrations.AlterModelTable(
            name='people',
            table='people',
        ),
        migrations.DeleteModel(
            name='Friend',
        ),
    ]
