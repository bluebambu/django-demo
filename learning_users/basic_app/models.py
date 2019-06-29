from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User) # it is like unique foreign key

    #
    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.name
