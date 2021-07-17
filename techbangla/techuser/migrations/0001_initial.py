# Generated by Django 3.2 on 2021-07-12 15:06

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
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(upload_to='profile_pic', verbose_name='Profile Picture')),
                ('about', models.TextField(verbose_name='About Yourself')),
                ('website', models.URLField(blank=True, default='http://127.0.0.1:8000/', verbose_name='Website/Blogs')),
                ('facebook', models.URLField(blank=True, default='http://127.0.0.1:8000/', verbose_name='Facebook Link')),
                ('twitter', models.URLField(blank=True, default='http://127.0.0.1:8000/', verbose_name='Twitter Link')),
                ('linkedin', models.URLField(blank=True, default='http://127.0.0.1:8000/', verbose_name='LinkedIn Link')),
                ('github', models.URLField(blank=True, default='http://127.0.0.1:8000/', verbose_name='Github Link')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
