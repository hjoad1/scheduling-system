from django.shortcuts import render
from rest_framework import viewsets
from .models import Subject, Tutor, Tutor_Subject, Student, Availability, Booking
from .serializers import SubjectSerializer, TutorSerializer, Tutor_SubjectSerializer, StudentSerializer, AvailabilitySerializer, BookingSerializer

# Create your views here.

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class TutorViewSet(viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer

class Tutor_SubjectViewSet(viewsets.ModelViewSet):
    queryset = Tutor_Subject.objects.all()
    serializer_class = Tutor_SubjectSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class AvailabilityViewSet(viewsets.ModelViewSet):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
