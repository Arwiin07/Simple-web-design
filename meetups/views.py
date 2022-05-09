from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    meetups=[
        {"title":"A first meetup","location":"NewYork","slug":"a-first-meetup"},
        {"title":"A second meetup","location":"Paris","slug":"a-second-meetups"}
    ]
    return render(request,"meetups/index.html",{
        "show_meetups":True ,
        "meetups":meetups
    })

def meetup_details(request,meetup_slug ):
    print(meetup_slug,'test')
    selected_meetup={
        "title":"A first meetup",
        "description":"Our first meetup!"
    }
    return render(request,"meetups/meetup-details.html",{
        "meetup_title":selected_meetup["title"],
        "meetup_description":selected_meetup["description"]
    })

# Create your views here.
