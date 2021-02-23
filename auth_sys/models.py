from django.db import models
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Point(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    user = models.ForeignKey('UserProfile', models.CASCADE)

    def __str__(self):
        return f"({self.x}; {self.y})"

    @classmethod
    def get_points(cls):
        return list(map(lambda point: {'x': point.x, 'y': point.y}, cls.objects.all()))


class UserProfile(models.Model):
    user = models.OneToOneField(User, models.CASCADE)

    def __str__(self):
        return f"Profile {self.username}"

    @property
    def username(self):
        return self.user.username
