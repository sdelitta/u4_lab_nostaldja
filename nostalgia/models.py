from django.db import models

class Decade(models.Model):
    start_year = models.TextField()

    def __str__(self):
        return self.start_year

class Fad(models.Model):
    name = models.TextField()
    image_url = models.TextField()
    description = models.TextField()
    decade = models.ForeignKey(
        Decade, on_delete=models.CASCADE, related_name='fads')

    def __str__(self):
        return self.name