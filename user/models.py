from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    class Meta:
        db_table = 'user'
    
    team_name = models.CharField(max_length=128, default='')