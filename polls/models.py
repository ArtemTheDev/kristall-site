from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class Customs(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    colors = models.CharField(max_length=100)


class Task(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField('Название новости', max_length=50)
    slug = models.SlugField(max_length=50, unique_for_date='publish', unique=True)
    task = models.TextField('Текст новости')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='polls_task', )

    img = models.ImageField(upload_to='images/', blank=True)

    object = models.Manager()
    published = PublishedManager()

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ('-publish',)

    def __str__(self):
        return self.title
