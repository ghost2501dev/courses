from django.db.models.functions import Substr, Upper
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic.detail import DetailView

from .models import Course, Class


def courses_view(request):
    if request.user.is_superuser:
        qs = Course.objects
    else:
        qs = Course.published_courses
    qs = qs.annotate(first_letter_name=Upper(Substr('name', 1, 1)))
    return render(request, 'courses/courses.html', {'courses': qs})


class CourseDetailView(DetailView):
    model = Course

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Course.objects.all()
        else:
            return Course.published_courses.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumb'] = (
            {'title': 'Cursos', 'url': reverse('courses:courses')},
            {'title': self.object.name},
        )
        return context


class ClassDetailView(DetailView):
    model = Class

    def get_object(self):
        is_published = True
        if self.request.user.is_superuser:
            is_published = False

        return get_object_or_404(
            Class,
            slug__iexact=self.kwargs['class_slug'],
            course__slug__iexact=self.kwargs['course_slug'],
            course__is_published=is_published,
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumb'] = (
            {'title': 'Cursos', 'url': reverse('courses:courses')},
            {'title': self.object.course.name, 'url': reverse('courses:course', args=[self.object.course.slug])},
            {'title': self.object.title},
        )
        return context
