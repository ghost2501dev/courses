from adminsortable.admin import NonSortableParentAdmin, SortableStackedInline

from django.contrib import admin

from .models import Course, Class


class ClassInline(SortableStackedInline):
    model = Class
    fields = ('title',)
    extra = 0
    max_num=0
    show_change_link = True


@admin.register(Course)
class CourseAdmin(NonSortableParentAdmin):
    fields = (
        'name', 'is_published', 'description', 'youtube_url', 'duration',
        'required_courses', 'meta_keywords', 'meta_description',
    )
    filter_horizontal = ('required_courses',)

    inlines = [
        ClassInline,
    ]


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    fields = ('title', 'course', 'content', 'meta_keywords', 'meta_description')
