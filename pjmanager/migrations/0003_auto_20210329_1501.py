# Generated by Django 3.1.7 on 2021-03-29 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pjmanager', '0002_projet_statut'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userhasprojet',
            name='projet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pjmanager.projet'),
        ),
    ]
