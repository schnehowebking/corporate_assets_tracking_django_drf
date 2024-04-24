from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)

class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

class Device(models.Model):
    TYPE_CHOICES = [
        ('phone', 'Phone'),
        ('tablet', 'Tablet'),
        ('laptop', 'Laptop'),
        ('other', 'Other'),
    ]
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    name = models.CharField(max_length=255)
    condition = models.TextField()

class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    checked_out_time = models.DateTimeField()
    checked_in_time = models.DateTimeField(null=True, blank=True)
    condition_when_checked_out = models.TextField()
    condition_when_returned = models.TextField(null=True, blank=True)