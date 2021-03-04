from django.db import models

from events.models import Event_category_model,Events_model, Event_keywords_model

# Create your models here.
class SimilarEvents(models.Model):
    event = models.OneToOneField(Events_model,on_delete=models.CASCADE,primary_key=True)
    similar_events = models.CharField(max_length=200)

class HistoryRecommendedEvents(models.Model):
    
    pass



    
