from django.db.models.functions import Substr, Upper
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic.detail import DetailView

from .models import Course, Class


def courses_view(request):
    qs = Course.objects.annotate(first_letter_name=Upper(Substr('name', 1, 1)))
    return render(request, 'courses/courses.html', {'courses': qs})


class CourseDetailView(DetailView):
    model = Course

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
        class_ = get_object_or_404(
            Class,
            slug__iexact=self.kwargs['class_slug'],
            course__slug__iexact=self.kwargs['course_slug'],
            course__is_published=True)
        return class_

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumb'] = (
            {'title': 'Cursos', 'url': reverse('courses:courses')},
            {'title': self.object.course.name, 'url': reverse('courses:course', args=[self.object.course.slug])},
            {'title': self.object.title},
        )
        return context
