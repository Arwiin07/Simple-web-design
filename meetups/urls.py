from django.urls import path
from . import views
urlpatterns=[
    path("",views.index,name="index"),
    path('meetups/<slug:meetup_slug>',views.meetup_details,name="meetups-detail"),   #ourdomain.com/meetups/a-second-meetups <dynamic>
]