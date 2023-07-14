# Generated by Django 3.2.15 on 2022-09-24 09:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='Created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='createdby', to=settings.AUTH_USER_MODEL),
        ),
    ]
