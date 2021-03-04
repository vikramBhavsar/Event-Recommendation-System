from django.shortcuts import render
from django.contrib.auth.models import User

from django.views import View
from django.http import HttpResponse
from django.http import JsonResponse


from events.models import Events_model,Event_keywords_model,Event_category_model

from django.views.decorators.csrf import csrf_exempt

import json

from HelperPack import help



def getCosineBetHistoryAndEvents(sorted_keywords,keywords_dictionary,user_keywords_set,max_spread,min_spread):

    recommendationForUser = {}



    for event in Events_model.objects.all():

        keywords = []
        score = []

        
        for keywo in  event.event_keywords.all():
            keywords.append(keywo.e_keyword)
            score.append(keywo.e_score)

        
        event_keywords = {}
        event_keywords_set = set()

        # calculating top 50% of the keywords
        end = int(len(keywords) * 50 /100)
        for i in range(end):
            event_keywords[keywords[i]] = float(score[i])
            event_keywords_set.add(keywords[i])

        # calculating top 20% of the keywords
        end = int((len(user_keywords_set) * 10 )/ 100)
        temp_user_keyword_set = set()
        for i in range(min(50,len(sorted_keywords))):
            temp_user_keyword_set.add(sorted_keywords[i][0])

        # print("-----------USERS KEYWORD SET---------")
        # print(temp_user_keyword_set)
        # unionizing the two set
        keyword_set = set()
        keyword_set = event_keywords_set.intersection(temp_user_keyword_set)
        # print("%s\t%s" % (index,keyword_set)

        # now finally calculating the cosine similarity
        # the moment we have all been waiting for. 
        eucli_user = 0
        eucli_event = 0
        cosine = 0
        
        #temporarily tracking the words that match
        words_list = []
        print("\nEvent Word List %s" % event_keywords_set)
        print("Word List for event %s %s is %s\n" % (event.pk,event.e_name,keyword_set))
        for keyw in keyword_set:
    #         print("(%s) %s  and %s" % (keyw,event_keywords[keyw],sorted_keywords[keyw]))
            
            normalized_user_score = (keywords_dictionary[keyw] - min_spread)/(max_spread-min_spread)        
            cosine += event_keywords[keyw] * (normalized_user_score)
    #         print("Cosine for %s is %s" % (keyw,normalized_user_score))
            eucli_user += normalized_user_score ** 2
            eucli_event += event_keywords[keyw] ** 2
            words_list.append(keyw)

        eucli_user = eucli_user ** 0.5
        eucli_event = eucli_event ** 0.5
        
        # calculating final similarity
        similarity = 0
        if eucli_user != 0 and eucli_event != 0:
            similarity = cosine / (eucli_user * eucli_event)        

        # cosine value for that event is added to the dictionary    
        if similarity > 0:
            recommendationForUser[event.pk] = similarity

    # sorting the events in decreasing order
    sorted_tuples = sorted(recommendationForUser.items(), key=lambda item: item[1],reverse=True)
    for item in sorted_tuples:
        print(item)


# Create your views here.
@csrf_exempt
def index(request):
    print("-------custom code from inside of recommender------")

    if request.method == 'GET':
        print("this is from inside of get function")
        
    elif request.method == 'POST':
        
        print("this is from inside of the recommender function")
        jsonHistory = json.loads(request.body)


        records = []

        latestAccessTime = 1

        for element in jsonHistory:
            if 'user_id' in element.keys():
                pass
                print("User_ID that was receieved was %s" % element["user_id"])
            elif 'title' in element.keys():
                record = [element["title"],element["url"],element["time"]]
                records.append(record)

                if element["time"] > latestAccessTime:
                    latestAccessTime = element["time"]

        # sending processed history to the helper class which contains
        # code that processes the history data
        stop_words = help.getStopWords()

        history_recommender = help.HistoryRecommendation()

        sorted_keywords,keywords_dictionary, user_keywords_set, max_spread, min_spread = history_recommender.main_driver(records,latestAccessTime,stop_words)

        # calculating cosine similarity now.
        getCosineBetHistoryAndEvents(sorted_keywords,keywords_dictionary, user_keywords_set, max_spread, min_spread)
        
        

    return HttpResponse("Hello world from recommender")


class HistoryRecommender(View):
    def get(self,request):
        pass

    def post(self,request):
        pass

        
