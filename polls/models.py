from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class Customs(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    colors = models.CharField(max_length=1, default='0')
    avatar = models.ImageField(upload_to='images/avatars/', default='images/avatars/default.png')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Customs.objects.create(user=instance)
        Customs.colors = '0'


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

    def get_absolute_url(self):
        return reverse('tasks:post_detail', args=[self.slug, self.id])

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ('-publish',)

    def __str__(self):
        return self.title
