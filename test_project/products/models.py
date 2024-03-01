from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Product(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    start_datetime = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    min_user_group = models.IntegerField(default=5)
    max_user_group = models.IntegerField(default=25)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        permissions = [
            ('can_read_edit_product', 'Can Read and Edit Product'),
            ('can_read_product', 'Can Read Product'),
        ]

    def __str__(self):
        return self.name

class Lesson(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    video_link = models.URLField()
    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return self.title

class Group(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    students = models.ManyToManyField(User, related_name='group_memberships')
    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.name

class ProductAccessRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    requested_at = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} -{self.product.name}"
