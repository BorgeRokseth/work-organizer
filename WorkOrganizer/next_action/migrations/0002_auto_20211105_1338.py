# Generated by Django 3.2.8 on 2021-11-05 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('next_action', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='actions',
        ),
        migrations.AddField(
            model_name='nextaction',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='actions', to='next_action.project'),
        ),
    ]
