from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# Id,name,author_id,price,description,is_published,image,category_id
class Ad(models.Model):
    IS_PUB = [
        (True, "Опубликовано"),
        (False, "Не опубликовано")
    ]
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField(max_length=500)
    is_published = models.BooleanField(choices=IS_PUB, default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="data/img", null=True, blank=True)
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
