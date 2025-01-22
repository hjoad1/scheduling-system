from django.core.management.base import BaseCommand
from django.db import connection
from scheduler.models import Timezone
import pytz

class Command(BaseCommand):
    help = "Populate the Timezones table with valid PostgreSQL timezones"

    def handle(self, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute("SELECT name FROM pg_timezone_names;")
            timezones = [row[0] for row in cursor.fetchall()]
        
        # Filter valid pytz-compatible timezones
        valid_timezones = [tz for tz in timezones if tz in pytz.all_timezones]
        
        # Save valid timezones to the database
        Timezone.objects.bulk_create([Timezone(name=tz) for tz in valid_timezones])
        
        self.stdout.write(self.style.SUCCESS('Successfully populated the Timezones table!'))
