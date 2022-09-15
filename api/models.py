from django.db import models

# Create your models here.
class apiModel(models.Model):
    string = models.CharField(max_length = 200)

    def __str__(self):
        return self.string