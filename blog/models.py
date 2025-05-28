from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='URL')
    description = models.TextField(blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.SlugField(unique=True, verbose_name='URL')
    content = RichTextField(verbose_name='Содержание')
    featured_image = models.ImageField(upload_to='posts/%Y/%m/%d/', verbose_name='Изображение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    tags = TaggableManager(verbose_name='Теги')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    reading_time = models.PositiveIntegerField(default=5, verbose_name='Время чтения (мин)')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='URL')
    description = models.TextField(verbose_name='Описание')
    featured_image = models.ImageField(upload_to='projects/%Y/%m/%d/', verbose_name='Изображение')
    demo_url = models.URLField(blank=True, verbose_name='Демо')
    github_url = models.URLField(blank=True, verbose_name='GitHub')
    technologies = TaggableManager(verbose_name='Технологии')
    is_featured = models.BooleanField(default=False, verbose_name='Избранный проект')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    bio = RichTextField(verbose_name='О себе', blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, verbose_name='Аватар')
    github_url = models.URLField(blank=True, verbose_name='GitHub')
    linkedin_url = models.URLField(blank=True, verbose_name='LinkedIn')
    twitter_url = models.URLField(blank=True, verbose_name='Twitter')
    skills = TaggableManager(verbose_name='Навыки')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f'Профиль {self.user.username}'
