from django.db import models

# Create your models here.
class ForumPost(models.Model):
    # TODO : implement how to get current user
    # main content of the Forum Post
    topic = models.CharField(max_length=140)
    description = models.CharField(max_length=1000)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.topic

# TODO: implement the thread class