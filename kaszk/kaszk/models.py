from django.db import models

# Create your models here.


class News(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    group = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.group}-{self.title}-{self.date}"
