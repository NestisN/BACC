from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import EmployeeViewSet, EmployeeInitialCodeViewSet
from .views import SubjectViewSet, SubjectExamViewSet, SubjectReportViewSet
from .views import ResponsibilityViewSet


router = DefaultRouter()
router.register(r'employee', EmployeeViewSet)
router.register(r'employeeInitialCode', EmployeeInitialCodeViewSet)
router.register(r'Subject', SubjectViewSet)
router.register(r'SubjectExam', SubjectExamViewSet)
router.register(r'SubjectReport', SubjectReportViewSet)
router.register(r'Responsibility', ResponsibilityViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
