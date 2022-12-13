from django.db import models

class Post(models.Model):

    user_id = models.ForeignKey("RareUser", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    publication_date = models.DateField()
    content = models.CharField(max_length=250)
    approved = models.BooleanField()
