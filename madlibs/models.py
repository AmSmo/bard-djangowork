from django.db import models

class Sonnet(models.Model):
    sonnet = models.IntegerField()

    def __str__(self):
        return ("Sonnet", self.sonnet)
