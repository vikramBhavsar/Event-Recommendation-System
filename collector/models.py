from django.db import models
from django.contrib.auth.models import User
from events.models import Events_model,Event_category_model,Event_keywords_model
import datetime

# Create your models here.

class Event_User_log(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    event = models.ForeignKey(Events_model,on_delete=models.CASCADE)
    timedetails = models.DateField(default=datetime.date.today)
    viewDetails = models.IntegerField(default=0)
    viewDate = models.IntegerField(default=0)
    viewLocation = models.IntegerField(default=0)
    viewRegistration = models.IntegerField(default=0)
    

    ######## assigning id's for easier access ######
    # viewRegistration = 1
    # viewLocation = 2
    # viewDate = 3
    # viewDetails = 4




