from django.db import models


from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    passwoed = models.TextField()

    def __str__(self):
        return self.name

from django.db import models

class ServiceRequest(models.Model):
    SERVICE_TYPES = [
        ('Installation', 'Installation'),
        ('Maintenance', 'Maintenance'),
        ('Repair', 'Repair'),
    ]
    reqid = models.AutoField(primary_key=True)
    service_type = models.CharField(max_length=100, choices=SERVICE_TYPES,default='Installation')
    description = models.TextField()
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)

    def __str__(self):
        return f"Service Request - {self.service_type}"


from django.db import models
from .models import ServiceRequest

class RequestStatus(models.Model):
    
    service_request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.service_request} - {self.status}"
