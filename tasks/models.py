from django.db import models
from django.utils.text import slugify
from django.conf import settings
from django.urls import reverse

from time import time

# Create your models here.


def gen_slug(name):
    slug = slugify(name, allow_unicode=True)
    return slug+'-'+str(int(time()))


class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=15, unique=True)
    spent_hours = models.IntegerField(blank=True)
    spent_minutes = models.IntegerField(blank=True)
    scheduled_hours = models.IntegerField(blank=True)
    scheduled_minutes = models.IntegerField(blank=True)
    data = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=250, blank=True)
    category = models.ManyToManyField('Category',
                                      related_name='tasks',blank=True)
    time_trigger = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)

    def get_hidden_url(self):
        return reverse('task_hidden_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('task_delete_url', kwargs={'slug': self.slug})

    def get_restore_url(self):
        return reverse('task_restore_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('task_update_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = gen_slug(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return (self.name + '-' + str(self.data.year) + '-' + str(self.data.month)
                + '-' + str(self.data.day) + ' Time:' + str(self.data.hour) + ':'
                + str(self.data.minute))


class Category(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=170, blank=True)
    total_time = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('category_view_url', kwargs={'slug':self.slug})

    def get_delete_url(self):
        return reverse('category_delete_url', kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):
        self.slug = gen_slug('category-' + self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
