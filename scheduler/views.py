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

    def get_queryset(self):
        queryset = super().get_queryset()
        subject_name = self.request.query_params.get('subject', None)
        if subject_name:
            # Filter tutors by the subject name
            queryset = queryset.filter(
                id__in=Tutor_Subject.objects.filter(subject__name=subject_name).values_list('tutor_id', flat=True)
            )
        return queryset

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
