from django.urls import path
from django.utils.translation import gettext_lazy as _

from .views import courses_view, CourseDetailView, ClassDetailView

app_name = 'courses'
urlpatterns = [
    path('', courses_view, name='courses'),
    path(_('cursos/<slug:slug>/'), CourseDetailView.as_view(), name='course'),
    path(_('cursos/<slug:course_slug>/<slug:class_slug>/'), ClassDetailView.as_view(), name='class'),
]
