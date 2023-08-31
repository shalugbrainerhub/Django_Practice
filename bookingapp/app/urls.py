
from django.urls import path, include
from . import views

urlpatterns = [
    path('slot', views.allTimeSlots, name='slot'),
    path('service', views.allServicesView, name='service'),
    path('', views.homeView, name='home'),
    path('appointment/<int:pk>', views.appointmentView, name='appointment'),
    path('book', views.bookAppointmentView, name='book'),
    path('addService', views.addServiceView, name='addService'),
    path('allBookings', views.allBookingsView, name='allBookings'),
    path('addSlot',views.addSlotsView, name='addSlot')
]
