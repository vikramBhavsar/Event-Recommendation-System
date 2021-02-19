from django.shortcuts import render
from .models import Events_model, Event_keywords_model,Event_category_model

from recommender.models import SimilarEvents

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

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        if 'category_pk' in self.kwargs:
            category_pk = self.kwargs["category_pk"]
            return Events_model.objects.filter(e_category=Event_category_model.objects.get(pk=category_pk))
            
        else:
            print("Normal GET function")

            return super().get_queryset()
    

    def get_context_data(self, **kwargs):

        # does not differentiate between passing the keywords and not passing the keywords
        # i.e website/events/  and  website/events/2

        context = super().get_context_data(**kwargs)
        context["categories"] = Event_category_model.objects.all()

        return context

class EventDetailView(DetailView):
    model = Events_model

    template_name = 'events/events_detail_views.html'

    context_object_name = "event"

    def get_context_data(self, **kwargs):

        # getting other similar events        
        print("----custom code----")
        cur_even_pk = self.kwargs['pk']

        similar_events_id = SimilarEvents.objects.get(pk=cur_even_pk)
        similar_events_id = similar_events_id.similar_events.split(' ')

        # converting values to integer
        similar_events_id_int = []
        for sim_id in similar_events_id:
            if sim_id.isnumeric():
                similar_events_id_int.append(int(sim_id))
        
        # similar_events = Events_model.objects.filter(pk__in=[similar_events_id_int[1:min(6,len(similar_events_id_int))]])   

        similar_events = Events_model.objects.filter(pk__in=similar_events_id_int[1:min(6,len(similar_events_id_int))])

        context = super().get_context_data(**kwargs)
        context['similar_events'] = similar_events
        print(context)
        
        return context

    


    
    
