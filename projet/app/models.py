from django.db import models

class Member(models.Model):
    nom = models.CharField(max_length=50)
    image_url = models.URLField(blank=True, max_length=1000)
    quote = models.CharField(max_length=100)


