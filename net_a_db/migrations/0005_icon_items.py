# Generated by Django 4.1 on 2024-03-09 16:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('net_a_db', '0004_fishinfo_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Icon_items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon_set', models.IntegerField(blank=True, default=0, null=True)),
                ('create_at', models.DateTimeField(default=datetime.datetime.now)),
                ('update_at', models.DateTimeField(default=datetime.datetime.now)),
                ('fish_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='net_a_db.fishinfo')),
                ('icon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='net_a_db.icon')),
            ],
        ),
    ]
