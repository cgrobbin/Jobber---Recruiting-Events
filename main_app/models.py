from django.db import models
from django.contrib.auth.models import User

# Create your models here.
FOCUS = (
    ('T', 'Tech'),
    ('M', 'Marketing'),
    ('C', 'Content Creation')
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    bio = models.TextField()

    

    def __str__(self):
        return f'{self.user.username}\'s Profile '

class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    time = models.CharField(max_length=25)
    speakers = models.CharField(max_length=250)
    focus = models.CharField(
        max_length=1,
        choices=FOCUS,
        default=FOCUS[0][0]
    )
    description = models.TextField()
    url = models.CharField(
        max_length=250,
        default='https://us05web.zoom.us/j/7915630422?pwd=Q2hnV2NnUEdFVTNYNUJRTWtHdDlzZz09'
        )
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.title