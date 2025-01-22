from rest_framework import serializers
from .models import Subject, Tutor, Tutor_Subject, Student, Availability, Booking
from django.utils.timezone import make_aware, datetime
from pytz import timezone

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = '__all__'

class Tutor_SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor_Subject
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class AvailabilitySerializer(serializers.ModelSerializer):
        class Meta:
            model = Availability
            fields = '__all__'

        def validate(self, data):
            is_recurring = data.get('is_recurring')
            date = data.get('date')

            # If `is_recurring` is True, `date` must be null
            if is_recurring and date is not None:
                raise serializers.ValidationError("If availability is recurring, the date must be null.")

            # If a date is provided, `is_recurring` must be False
            if date is not None and is_recurring:
                raise serializers.ValidationError("If a date is provided, availability cannot be recurring.")

            # If `is_recurring` is False, a date must be provided
            if not is_recurring and date is None:
                raise serializers.ValidationError("If availability is not recurring, a date must be provided.")

            return data

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def validate(self, data):
        tutor = data.get('tutor')
        student = data.get('student')
        date = data.get('date')
        start_time = data.get('start_time')
        end_time = data.get('end_time')

        # Retrieve the timezones from PostgreSQL and use them
        tutor_tz_name = tutor.timezone.name
        student_tz_name = student.timezone.name

        # Convert to Python's timezone objects
        tutor_tz = timezone(tutor_tz_name)
        student_tz = timezone(student_tz_name)

        # Make the start_time and end_time timezone-aware in the student's timezone
        student_start_time = make_aware(datetime.combine(date, start_time), student_tz)
        student_end_time = make_aware(datetime.combine(date, end_time), student_tz)

        # Convert the times to the tutor's timezone
        tutor_start_time = student_start_time.astimezone(tutor_tz)
        tutor_end_time = student_end_time.astimezone(tutor_tz)

        # Extract the day of the week in the tutor's timezone
        tutor_day_of_week = tutor_start_time.weekday()

        # Step 1: Check if the tutor is available at the requested time in their timezone
        available_slots = Availability.objects.filter(
            tutor=tutor,
            day_of_week=tutor_day_of_week,  # Day of the week in tutor's timezone
            start_time__lte=tutor_start_time.time(),  # Compare times only
            end_time__gte=tutor_end_time.time(),
        ).filter(
            is_recurring=True  # Recurring availability
        ) | Availability.objects.filter(
            tutor=tutor,
            date=date,  # Match the exact date for one-time availability
            start_time__lte=tutor_start_time.time(),
            end_time__gte=tutor_end_time.time(),
        )

        if not available_slots.exists():
            raise serializers.ValidationError("The tutor is not available at the requested time in their timezone.")

        # Step 2: Check for overlapping bookings in the tutor's timezone
        overlapping_bookings = Booking.objects.filter(
            tutor=tutor,
            date=date,  # Same date
        ).filter(
            start_time__lt=end_time,  # Overlaps if existing booking starts before the new booking ends
            end_time__gt=start_time,  # Overlaps if existing booking ends after the new booking starts
        )

        if overlapping_bookings.exists():
            raise serializers.ValidationError("The requested time slot overlaps with an existing booking.")

        return data
