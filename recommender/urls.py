from django.urls import path

from . import views


urlpatterns = [
    # path('', views.index, name='index'),
    path('index/',views.index,name='recommender-index'),
    path('history_recommendations/',views.HistoryRecommender.as_view(),name='history-recommendations'),
    
]