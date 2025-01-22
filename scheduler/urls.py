from rest_framework.routers import DefaultRouter
from .views import SubjectViewSet, TutorViewSet, Tutor_SubjectViewSet, StudentViewSet, AvailabilityViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'subjects', SubjectViewSet)
router.register(r'tutors', TutorViewSet)
router.register(r'tutor_subjects', Tutor_SubjectViewSet)
router.register(r'students', StudentViewSet)
router.register(r'availability', AvailabilityViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = router.urls
