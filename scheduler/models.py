from django.db import models

# Create your models here.

class Timezone(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
    
class Tutor(models.Model):
    name = models.CharField(max_length=255)
    timezone = models.ForeignKey(Timezone, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=255)
    timezone = models.ForeignKey(Timezone, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Availability(models.Model):
    DAYS_OF_WEEK = [
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    ]
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    day_of_week = models.IntegerField(choices=DAYS_OF_WEEK)
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_recurring = models.BooleanField(default=False)
    date = models.DateField(null=True, blank=True)  # For one-time availability

    def __str__(self):
        return f"{self.tutor.name} - {self.day_of_week} ({self.start_time}-{self.end_time})"
    
class Booking(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.student.name} booked {self.tutor.name} on {self.date}"
