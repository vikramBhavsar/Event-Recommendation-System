from django.shortcuts import render
from .models import Events_model, Event_keywords_model,Event_category_model
from django.contrib.auth.models import User

from recommender.models import SimilarEvents
from collector.models import Event_User_log

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.
def index(request):

    data_obj = Event_category_model.objects.all()

    count = 0

    courousel_list = []
    obj_list = []

    for obj in data_obj:
        obj_list.append(obj)
        count += 1

        if count == 3:
            print(obj_list)
            count = 0
            courousel_list.append(obj_list)
            obj_list = []
        
    print(courousel_list)
    # for obj in data_obj:
    #     obj_list.append(obj)

    

    return render(request,"events/temp.html",{"data_obj":courousel_list})

class EventsListView(ListView):

    model = Events_model
    template_name = 'events/events_list_views.html'
    context_object_name = "events"

    def get(self, request, *args, **kwargs):
        print(kwargs)
        return super().get(request, *args, **kwargs)

    def get_queryset(self): 
        if 'category_pk' in self.kwargs:
            category_pk = self.kwargs["category_pk"]
            return Events_model.objects.filter(e_category=Event_category_model.objects.get(pk=category_pk))
            
        else:
            print("\t\t\tNormal GET function")
            

            # checking if user has searched for any events
            if 'search_q' in self.request.GET:
                search_term = self.request.GET["search_q"]
                
            else:
                print("Normal search is taking place.")

            return super().get_queryset()
    

    def get_context_data(self, **kwargs):

        # does not differentiate between passing the keywords and not passing the keywords
        # i.e website/events/  and  website/events/2

        context = super().get_context_data(**kwargs)
        context["categories"] = Event_category_model.objects.all()

        if self.request.user.is_authenticated:

            recommends = get_recs_based_on_click_events(self.request.user)
            print("user is authenticated")

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

# other methods
def get_recs_based_on_click_events(user):
    print("---custom code--")
    print(user)
    print(user.id)
    print(type(user))

    cu_user = User.objects.get(pk=user.id)

    evidences = Event_User_log.objects.filter(user=cu_user)
    # print(evidences)


    # calculating score:
    for evidence in evidences:
        score = 0
        # print("[+] Investigation %s" % evidence)
        if evidence.viewRegistration > 0:
            score += 100
            # print("Has Viewed Registration")
        
        # checking view date and location together. (very strong chance the user is intrested)
        if evidence.viewDate > 0 and evidence.viewLocation > 0:
            score += 80
        elif evidence.viewDate > 0 or evidence.viewLocation > 0:
            score += 40
        
        if evidence.viewDetails > 0:
            score += 20

        # print("Final Score is - %s for %s" % (score,evidence))



        


    
    # for reference
    # timedetails = models.DateField(default=datetime.date.today)
    # viewDetails = models.IntegerField(default=0)
    # viewDate = models.IntegerField(default=0)
    # viewLocation = models.IntegerField(default=0)
    # viewRegistration = models.IntegerField(default=0)
    


    
    
