from adminsortable.models import SortableMixin
from ckeditor.fields import RichTextField
from slugify import slugify

from django.db import models
from django.urls import reverse


class CourseIsPublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)


class Course(models.Model):
    name = models.CharField('Nombre', max_length=128, blank=False, unique=True)
    description = RichTextField(verbose_name='Descripción', default='', blank=True)
    youtube_url = models.CharField('URL en Youtube', max_length=256, default='', blank=True)
    duration = models.IntegerField('Duración del curso', blank=True, null=True)
    slug = models.CharField('Slug', max_length=128, blank=False, unique=True)
    is_published = models.BooleanField('Está publicado', default=False)
    meta_keywords = models.CharField('Meta keywords', max_length=255, default='', blank=True)
    meta_description = models.CharField('Meta description', max_length=155, default='', blank=True)

    required_courses = models.ManyToManyField(
        'Course', blank=True, verbose_name='Cursos requeridos')

    objects = models.Manager()
    published_courses = CourseIsPublishedManager()

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('courses:course', args=[self.slug])


class Class(SortableMixin):
    title = models.CharField('Título', max_length=128, blank=False)
    slug = models.CharField('Slug', max_length=128, blank=False)
    content = RichTextField(verbose_name='Contenido')
    order = models.PositiveIntegerField('Orden', default=0, editable=False, db_index=True)
    meta_keywords = models.CharField('Meta keywords', max_length=255, default='', blank=True)
    meta_description = models.CharField('Meta description', max_length=155, default='', blank=True)

    course = models.ForeignKey(
        Course, null=True, on_delete=models.SET_NULL, verbose_name='Curso')

    class Meta:
        verbose_name = 'Clase'
        verbose_name_plural = 'Clases'
        ordering = ['order']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('courses:class', args=[self.course.slug, self.slug])

    def get_previous(self):
        return super().get_previous([('course', self.course)])

    def get_next(self):
        return super().get_next([('course', self.course)])
