# Generated by Django 2.2.6 on 2019-10-29 07:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('house', models.ImageField(default='', upload_to='photos/house')),
                ('tree', models.ImageField(default='', upload_to='photos/tree')),
                ('person', models.ImageField(default='', upload_to='photos/person')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_photos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
