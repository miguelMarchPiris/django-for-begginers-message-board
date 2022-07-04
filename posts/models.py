from django.db import models


class Post(models.Model):
    text = models.TextField()
    num = models.IntegerField()

    def __str__(self):
        return f"{self.text[:50]}{self.num}"
