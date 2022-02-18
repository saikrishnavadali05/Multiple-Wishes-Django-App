from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User , on_delete = models.CASCADE)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})

class CustomerHBD(models.Model):
    name = models.CharField(max_length=200)
    message = models.TextField()
    email = models.EmailField(max_length=50)
    date = models.DateField(max_length=50)
    time = models.TimeField()

    def __str__(self):
        return f"{self.date}"
#f"{self.name, self.message, self.email, self.date, self.time}"

class dummy(models.Model):
    name = models.CharField(max_length = 4)