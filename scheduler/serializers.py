from rest_framework import serializers
from .models import Subject, Tutor, Tutor_Subject, Student, Availability, Booking

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
