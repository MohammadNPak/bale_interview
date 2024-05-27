from django.db import models

# Create your models here.


class UrlModel(models.Model):
    url = models.URLField()
    short_url = models.CharField(max_length=256,blank=True)

    def __str__(self) -> str:
        return self.url+" | "+self.short_url
    