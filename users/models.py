from django.db import models
from django.utils.translation import gettext_lazy as _


# id,name,lat,lng
class Location(models.Model):
    name = models.CharField(max_length=200, unique=True)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Местоположение"
        verbose_name_plural = "Местоположения"


class UserRoles(models.TextChoices):
    MEMBER = 'member', _("member")
    MODERATOR = 'moderator', _("moderator")
    ADMIN = 'admin', _("admin")


# id,first_name,last_name,username,password,role,age,location_id
class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(choices=UserRoles.choices, max_length=9)
    age = models.PositiveSmallIntegerField()
    location = models.ManyToManyField(Location)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["username"]
