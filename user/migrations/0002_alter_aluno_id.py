# Generated by Django 4.2.5 on 2023-10-24 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]