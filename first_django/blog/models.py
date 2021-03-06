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
        return self.title 

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})

class customerHBD(models.Model):
    name= models.CharField(max_length=200)
    message = models.TextField()
    email = models.EmailField(max_length=50)
    date = models.DateField(max_length=50)
    time = models.TimeField()

    def __str__(self):
        return self.name