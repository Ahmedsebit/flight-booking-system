import urllib.request
import random
import os
import re

from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.files.temp import NamedTemporaryFile

from flight.models import Flight
from seats.models import Seat
from bookings.models import Booking
from customer_account.models import CustomerAccount
from user.models import CustomUser
from user.forms import CustomUserCreationForm, ImageUploadForm

def home(request):
    return render(request, "home.html", {})

def index(request):
    return render(request, "index.html", {})

def book(request, pk):
    flight = Flight.objects.get(id=pk)
    seats = Seat.objects.all()
    bookings = Booking.objects.filter(flight__id=flight.id)
    user = CustomerAccount.objects.get(id=request.user.id)
    booked_seats = []
    for booking in bookings:
        booked_seats.append(booking.seat)
    context = {'user':user,'flight': flight,'seats':seats,'booked_seats':booked_seats}
    return render(request, "book.html", context)

def profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    request_user = request.user
    context = {'user':user, 'request_user':request_user}
    return render(request, "profile.html", context)

def SaveProfile(request):
   saved = False
   user = CustomUser.objects.get(id=request.user.id)
   request_user = request.user
   context = {'user':user, 'request_user':request_user}
   if request.method == "POST":
      #Get the posted form
      form = ImageUploadForm(request.POST, request.FILES)
      
      if form.is_valid():
         user = CustomUser.objects.get(id=request.user.id)
         user.image = form.cleaned_data["image"]
         print(user.username)
         user .save()
         saved = True
   else:
      MyProfileForm = CustomUserCreationForm()
		
   return render(request, 'profile.html', context)


def download_image(request):
    user = CustomUser.objects.get(id=request.user.id)
    user = CustomUser.objects.get(id=request.user.id)
    request_user = request.user
    context = {'user':user, 'request_user':request_user}
    baseurl = request.build_absolute_uri()[:-10]
    url = baseurl + user.image.url

    dir = os.path.join('usr', 'test.html')
    file_name = random.randrange(1,10000)
    full_file_name = str(file_name) + '.jpg'
    desktop_file = os.path.expanduser("~/Desktop/"+full_file_name)
    urllib.request.urlretrieve(url,desktop_file )

    return redirect('profile')


def regular_expresion(request):
    user = CustomUser.objects.get(id=request.user.id)
    lst = []
    if request.POST:
        myfile = request.FILES['regular_expression'].read()
        phrase = myfile.decode("utf-8")
        if request.POST.get('type') == 'search':
            phrases = re.findall('\w+', phrase)
            for phrase in phrases:
                matches = re.search(r''+request.POST.get('text'), phrase)
                if matches is not None:
                    lst.append(matches.group())
        elif request.POST.get('type') == 'match':
            phrases = re.findall('\w+', phrase)
            for phrase in phrases:
                matches = re.match(r''+request.POST.get('text'), phrase)
                if matches is not None:
                    lst.append(matches.group())
        elif request.POST.get('type') == 'findall':
            matches = re.findall(request.POST.get('text'), phrase)
        elif request.POST.get('type') == "split":
                matches = re.split(request.POST.get('text'), phrase)
        obj = {"test":lst}
    else:
        obj={"test":"no date"}

    context = {'obj':obj}

    return render(request, "regular_expresion.html", context)