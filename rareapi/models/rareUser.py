from django.db import models

class RareUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.CharField(max_length=250)
    profile_image_url = models.ImageField('profileimages', height_field=None,
        width_field=None, max_length=None, null=True)
