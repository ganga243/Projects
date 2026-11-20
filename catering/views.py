from django.shortcuts import render, redirect
from .models import Booking

def booking(request):
    return render(request, 'booking.html')

    if request.method == 'POST':

        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        event_type = request.POST['event_type']
        event_date = request.POST['event_date']
        location = request.POST['location']
        guests = request.POST['guests']
        food_preference = request.POST['food_preference']
        requirements = request.POST['requirements']

        Booking.objects.create(
            name=name,
            phone=phone,
            email=email,
            event_type=event_type,
            event_date=event_date,
            location=location,
            guests=guests,
            food_preference=food_preference,
            requirements=requirements
        )

        return render(request, 'booking.html', {
            'success': 'Your booking submitted successfully!'
        })

    return render(request, 'booking.html')

# Create your views here.
