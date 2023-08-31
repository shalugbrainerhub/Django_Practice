from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from .models import *
from .forms import *

# Create your views here.


def homeView(request):
    return render(request,'app/home.html')


def allTimeSlots(request):
    allSlots=TimeSlot.objects.all()
    return render(request, 'app/slots.html', {'allSlots': allSlots})


def allServicesView(request):
    allServices=Service.objects.all()
    return render(request, 'app/service.html', {'allServices':allServices})


def appointmentView(request, pk):
    appointment= get_object_or_404(Appointment, id=pk)
    print(appointment)
    if appointment:
        return render(request, 'app/appointment.html', {'appointment':appointment})
    
    else:
        return HttpResponse("Something wrong")
    



def bookAppointmentView(request):
    print("I am booking")
    if request.method=='POST':
        print("With form")
        form=AppointmentForm(request.POST)
        print("With form")
        if form.is_valid():
           form.save()
           return redirect('home')

    else:
        form=AppointmentForm()


    return render(request, 'app/bookAppointment.html', {'form':form})
        


def addServiceView(request):
    if request.method=='POST':
        form=ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service')
        
    else:
        form=ServiceForm()

    return render(request, 'app/addService.html', {'form':form})



def allBookingsView(request):
    allBooking=Appointment.objects.all()
    return render(request, 'app/allBooking.html', {'allBooking':allBooking})




def addSlotsView(request):
    if request.method=='POST':
        form=SlotForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
        form=SlotForm()

    return render(request, 'app/addSlot.html', {'form':form})