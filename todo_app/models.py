from django.db import models
from django.urls import reverse

class Todo(models.Model):
    title = models.CharField(max_length=200,unique=True)
    complete = models.BooleanField(default=False)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('new_task', args=[str(self.id)])