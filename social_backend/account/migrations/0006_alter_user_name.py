# Generated by Django 4.2.5 on 2023-09-30 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_user_people_you_may_know'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
