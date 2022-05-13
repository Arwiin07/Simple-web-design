from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Meetup,participant
from.forms import RegistrationForm

def index(request):
    meetups=Meetup.objects.all()
    return render(request,"meetups/index.html",{
        "meetups":meetups
    })

def meetup_details(request,meetup_slug ):
    # import pdb;pdb.set_trace()
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        if request.method=="GET":
            registration_forms=RegistrationForm()
        else:
            registration_forms=RegistrationForm(request.POST)
            if registration_forms.isvalid():
                user_email=registration_forms.cleaned_data["email"]
                participants,_=participant.objects.get_or_create(email=user_email)
                selected_meetup.participants.add(participant)
                return redirect("confirm-registration")
        return render(request, "meetups/meetup-details.html", {
                "meetup_found": True,
                "meetup": selected_meetup,
                "form": registration_forms
                })



    except Exception as ex:
        print(ex)
        return render(request,"meetups/meetup-details.html",{
            "meetup_found":False
        })


# Create your views here.
def confirm_registration(request):
    return render(request,"meetups/registration-success.html")