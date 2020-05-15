from django.db import models


class Cowsay(models.Model):
    cowsay_string = models.TextField()

    def __str__(self):
        return self.cowsay_string
