from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
import re
from .models import Event, places
from datetime import datetime, timedelta
from django.core.paginator import Paginator
from django.utils import timezone


def index(request):
    place = places.objects.all().order_by('id')
    return render(request, 'index.html',{'place': place})

def contact(request):
    fname = request.POST.get('name')
    from_email = request.POST.get('email')
    from_feedback=request.POST.get('feedback')
    if re.match(r'^[\w\.-]+@[\w\.-]+$', from_email):
            touseremail = EmailMessage(
                subject=f'You have received feedback from {fname} on SIT_SLOT',
                body=f'{from_feedback}',
                from_email=settings.EMAIL_HOST_USER,
                to=['prathampshetty99@gmail.com'],
                cc=[],
            ).send()
    return render(request, 'contact.html')

def success(request):
    return render(request, 'event.html')

def book(request, place_id):
    place_id = place_id
    return render(request, 'book.html',{'place_id':place_id})

def bookslot(request): 
    if request.method == 'POST':
        place_id = request.Post.get('place_id')
        place = places.objects.get(pk=place_id)
        fname = request.POST.get('name')
        from_email = request.POST.get('email')
        date_str = request.POST.get('date')
        time_str = request.POST.get('time')
        duration = int(request.POST.get('duration'))  
        img = request.FILES.get('photo')
        
       
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        time = datetime.strptime(time_str, '%H:%M').time()
        
        # Calculate end time based on start time and duration
        start_datetime = timezone.make_aware(datetime.combine(date, time))
        end_datetime = start_datetime + timedelta(hours=duration)
        
        # Check if start time is before end time
        if start_datetime >= end_datetime:
            messages.error(request, "End time should be after start time")
            return render(request, 'book.html')

        # Check for overlapping bookings
        overlapping_bookings = Event.objects.filter(place=place,date=date, start_time__lt=end_datetime, end_time__gt=start_datetime)
        if overlapping_bookings.exists():
            email = EmailMessage(
                subject=f'Slot already booked for this time',
                body=f'Here is the message. {fname} {from_email}',
                from_email=settings.EMAIL_HOST_USER,
                to=[from_email],
                cc=[],
            ).send()
            return redirect('book')

        # Send email and save booking if everything is valid
        if re.match(r'^[\w\.-]+@[\w\.-]+$', from_email):
            query = Event(name=fname, email=from_email, date=date, start_time=start_datetime, end_time=end_datetime, image=img)
            query.save()
            email = EmailMessage(
                subject=f'{fname}',
                body=f'Here is the message. {fname} {from_email}',
                from_email=settings.EMAIL_HOST_USER,
                to=['snapship43@gmail.com'],
                cc=[],
            )
            email.attach(img.name, img.read(), img.content_type)
            email.send()
            touseremail = EmailMessage(
                subject=f'{fname}',
                body=f'your slot is booked  {fname} {from_email}',
                from_email=settings.EMAIL_HOST_USER,
                to=[from_email],
                cc=[],
            ).send()
          
            return redirect('event') 
        else:
            messages.error(request, "Invalid email address")
    
    return render(request, 'book.html')


def event(request):
    events = Event.objects.all().order_by('start_time')
    
    current_time = timezone.now()
    
    future_events = []
    
    for event in events:
        if event.start_time >= current_time:
            future_events.append(event)
  
    for event in events:
        if event not in future_events:
            event.delete()
            
    return render(request, 'event.html', {'events': future_events})
   
   
    