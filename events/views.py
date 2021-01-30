from django.shortcuts import render
from .models import Events_model, Event_keywords_model

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.
def index(request):
    # context = {: }?

    event_data = Events_model.objects.all()
    context = {"events":event_data}
    return render(request,"events/events_list_views.html",context)



class EventsListView(ListView):

    model = Events_model
    template_name = 'events/events_list_views.html'
    context_object_name = "events"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context[""] = 
        return context



class EventDetailView(DetailView):
    model = Events_model

    template_name = 'events/events_detail_views.html'

    context_object_name = "event"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    


    
    
