# Generated by Django 2.2.4 on 2019-08-02 13:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0004_auto_20190802_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bucketlist',
            name='owner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='buketlists', to=settings.AUTH_USER_MODEL),
        ),
    ]
