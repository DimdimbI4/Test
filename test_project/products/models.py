from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    start_datetime = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    min_user_group = models.IntegerField(default=5)
    max_user_group = models.IntegerField(default=25)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    video_link = models.URLField()

    def __str__(self):
        return self.title

class Group(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    students = models.ManyToManyField(User, related_name='group_memberships')

    def __str__(self):
        return self.name
