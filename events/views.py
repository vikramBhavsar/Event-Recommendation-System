from django.shortcuts import render
from .models import Events_model

# Create your views here.
def index(request):
    # context = {: }?

    event_data = Events_model.objects.all()
    context = {"events":event_data}
    return render(request,"events/events_list_views.html",context)