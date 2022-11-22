from django.db import models
#import models

from django.contrib.auth.models import User
class UserPreferences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    currency = models.CharField(max_length=3, blank=True , default='INR')

    def __str__(self):  
        return self.user.username 