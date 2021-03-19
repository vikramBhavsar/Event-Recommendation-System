from django.db import models
from django.contrib.auth.models import User
from events.models import Event_category_model
from datetime import datetime

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    age = models.IntegerField()
    category = models.ManyToManyField(Event_category_model)
    history_enabled = models.BooleanField(default=False)
    birth_date = models.DateField(null=True,blank=True)


class UserSearch(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    search_term = models.TextField()
    time_details = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.user.first_name + " - " + self.search_term

