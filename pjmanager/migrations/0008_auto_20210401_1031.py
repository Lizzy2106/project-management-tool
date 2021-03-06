# Generated by Django 3.1.7 on 2021-04-01 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pjmanager', '0007_auto_20210331_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projet',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pjmanager.type'),
        ),
        migrations.AlterField(
            model_name='userhasprojet',
            name='user_statut',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Responsable'), (2, 'Participant'), (3, 'Superviseur')], default=2),
        ),
    ]
