# Generated by Django 2.2.2 on 2019-06-28 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lobqr19', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='QuarterlyReport',
        ),
        migrations.RemoveField(
            model_name='qr2019',
            name='lobbyist_name',
        ),
        migrations.AddField(
            model_name='qr2019',
            name='dummy',
            field=models.CharField(default='default', max_length=127),
        ),
    ]
