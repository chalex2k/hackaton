# Generated by Django 3.1.7 on 2023-04-27 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contest',
            name='employer',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='contest',
            name='image_path',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='contest',
            name='format',
            field=models.TextField(choices=[(0, 'task_based'), (1, '???')], default=0),
        ),
    ]
