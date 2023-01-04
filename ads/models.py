from django.db import models


class Ads(models.Model):
    IS_PUB = [
        (True, "Опубликовано"),
        (False, "Не опубликовано")
    ]
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    description = models.TextField(max_length=500)
    address = models.CharField(max_length=100)
    is_published = models.BooleanField(choices=IS_PUB, default=False)

    def __str__(self):
        return self.name


class Categories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
