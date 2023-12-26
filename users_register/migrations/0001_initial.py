# Generated by Django 4.2 on 2023-12-26 02:27

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
            name='PostData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=100)),
                ('content_body', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('content_type', models.CharField(choices=[('Technology', 'Technology'), ('Entertainment', 'Entertainment'), ('Politics', 'Politics'), ('Food', 'Food')], max_length=100, null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
