from django.db import models
from django.contrib.auth.models import User
from events.models import Event_category_model

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    age = models.IntegerField()
    category = models.ManyToManyField(Event_category_model)
    history_enabled = models.BooleanField(default=False)
    birth_date = models.DateField(null=True,blank=True)


