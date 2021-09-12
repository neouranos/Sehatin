# Generated by Django 3.2.7 on 2021-09-12 10:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sehat_in_webproject', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=models.SET('deleted'), to=settings.AUTH_USER_MODEL),
        ),
    ]
