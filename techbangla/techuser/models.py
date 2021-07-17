from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    profile_pic = models.ImageField(upload_to='profile_pic', verbose_name="Profile Picture", blank=True)
    about = models.TextField(verbose_name="About Yourself", blank=True)
    website = models.URLField(verbose_name="Website/Blogs", blank=True)
    facebook = models.URLField(verbose_name="Facebook Link", blank=True)
    twitter = models.URLField(verbose_name="Twitter Link", blank=True)
    linkedin = models.URLField(verbose_name="LinkedIn Link", blank=True)
    github = models.URLField(verbose_name="Github Link", blank=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}\'s About'

