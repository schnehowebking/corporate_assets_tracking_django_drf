from rest_framework import serializers
from .models import Company, Employee, Device, DeviceLog

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class DeviceLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceLog
        fields = '__all__'
