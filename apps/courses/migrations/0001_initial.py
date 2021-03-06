# Generated by Django 3.0.11 on 2021-01-07 02:20

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Nombre')),
                ('description', models.TextField(blank=True, default='', verbose_name='Descripción')),
                ('youtube_url', models.CharField(blank=True, default='', max_length=256, verbose_name='URL en Youtube')),
                ('duration', models.IntegerField(blank=True, null=True, verbose_name='Duración del curso')),
                ('slug', models.CharField(max_length=128, unique=True, verbose_name='Slug')),
                ('is_published', models.BooleanField(default=False, verbose_name='Está publicado')),
                ('meta_keywords', models.CharField(blank=True, default='', max_length=255, verbose_name='Meta keywords')),
                ('meta_description', models.CharField(blank=True, default='', max_length=155, verbose_name='Meta description')),
                ('required_courses', models.ManyToManyField(blank=True, to='courses.Course', verbose_name='Cursos requeridos')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Título')),
                ('slug', models.CharField(max_length=128, verbose_name='Slug')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Contenido')),
                ('order', models.PositiveIntegerField(db_index=True, default=0, editable=False, verbose_name='Orden')),
                ('meta_keywords', models.CharField(blank=True, default='', max_length=255, verbose_name='Meta keywords')),
                ('meta_description', models.CharField(blank=True, default='', max_length=155, verbose_name='Meta description')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.Course', verbose_name='Curso')),
            ],
            options={
                'verbose_name': 'Clase',
                'verbose_name_plural': 'Clases',
                'ordering': ['order'],
            },
        ),
    ]
