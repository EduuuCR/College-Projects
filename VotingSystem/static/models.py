from django.db import models
from django.contrib.auth.models import User

class Competition(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='entries/')
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.title
