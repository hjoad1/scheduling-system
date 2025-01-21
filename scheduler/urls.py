from rest_framework.routers import DefaultRouter
from .views import TutorViewSet, StudentViewSet, AvailabilityViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'tutors', TutorViewSet)
router.register(r'students', StudentViewSet)
router.register(r'availability', AvailabilityViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = router.urls
