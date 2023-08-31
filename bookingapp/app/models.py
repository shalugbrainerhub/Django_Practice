from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Service(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.IntegerField()
    duration=models.DurationField()




class TimeSlot(models.Model):
    start=models.DateTimeField()
    end=models.DateTimeField()
    services=models.ForeignKey(Service, on_delete=models.CASCADE)
    capacity=models.PositiveIntegerField()
    available=models.BooleanField()

    def __str__(self):
        return f"{self.start}, {self.services.name}"
    
   






class Appointment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    timeslots=models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    status=models.CharField(max_length=30, choices=[('booked', 'Booked'), ('cancelled', 'Cancelled')])
    payment_status=models.BooleanField(default=False)
    reminder_status=models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    