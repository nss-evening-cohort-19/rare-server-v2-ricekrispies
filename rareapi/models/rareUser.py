from django.db import models

class RareUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.CharField(max_length=250)
    email = models.CharField(max_length=50)
    created_on = models.DateField()
    active = models.BooleanField()
    is_staff = models.BooleanField()
    profile_image_url = models.ImageField('profileimages', height_field=None,
        width_field=None, max_length=None, null=True)
