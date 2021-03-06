from django.db import models
from django.contrib.auth.models import User #extending User models that django provided
from django.db.models.signals import post_save 
from django.contrib.auth.models import User
from django.dispatch import receiver #decorator catch the signal called post_save

from PIL import Image

STATUS_CHOICES=(
    ("Infected", "Infected"),
    ("Not Infected", "Not Infected"),
)
VACCINATED_CHOICES=(
    ("Fully Vaccinated", "Fully Vaccinated"),
    ("Not Vaccinated", "Not Vaccinated"),
    ("First Dose", "First Dose"),
)

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # means: the user deleted, also the profile deleted in database(NOT for vice-versa)
    avatar = models.ImageField(default='default.jpg', upload_to='avatar_pict')
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(default='youremail@company.com', blank=False)
    phone = models.CharField(default='', max_length=20, blank=False)
    city = models.CharField(default='', max_length=100, blank=False)
    bio = models.TextField(default='', max_length=250, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Not Infected", blank=False)
    vaccinated_status = models.CharField(max_length=50,choices=VACCINATED_CHOICES, default="", blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} Profile' # out: username Profile

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # resize avatar to speed up website
        img = Image.open(self.avatar.path)
        if img.height > 350 or img.width > 350:
            out_size = (350,350)
            img.thumbnail(out_size)
            img.save(self.avatar.path)