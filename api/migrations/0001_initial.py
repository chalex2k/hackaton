# Generated by Django 3.1.7 on 2023-04-27 12:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('datetime_start', models.DateTimeField()),
                ('datetime_end', models.DateTimeField()),
                ('city', models.TextField(blank=True)),
                ('format', models.IntegerField(choices=[(0, 'task_based'), (1, '???')], default=0)),
                ('feeding', models.BooleanField()),
                ('difficulty', models.IntegerField()),
                ('type', models.IntegerField(choices=[(0, 'individual'), (1, 'command')], default=0)),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='contests', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-datetime_start'],
            },
        ),
    ]
