from rest_framework import serializers
from .models import Tutor, Student, Availability, Booking

class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class AvailabilitySerializer(serializers.ModelSerializer):
        class Meta:
            model = Availability
            fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
