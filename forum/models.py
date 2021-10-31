from django.db import models
from django.utils.text import slugify
# Create your models here.
class ForumPost(models.Model):
    # TODO : implement how to get current user
    # main content of the Forum Post
    topic = models.CharField(max_length=140)
    description = models.CharField(max_length=1000)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    slug = models.SlugField(default=slugify(topic))

    def __str__(self):
        return self.topic

    def snippets(self):
        if len(self.description) <= 100:
            return self.description
        else:
            return self.description[:100] + "..."

# TODO: implement the thread class