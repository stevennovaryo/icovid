from django.db import models

# Create your models here.
class forum(models.Model):
    topic = models.CharField()
    description = models.CharField()
    link = models.CharField()
    date_created = models.DateTimeField(auto_now_add=True,null=True)