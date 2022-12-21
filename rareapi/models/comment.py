from django.db import models
from .post import Post

class Comment(models.Model):

    user = models.ForeignKey("RareUser", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_on = models.DateField()
    content = models.CharField(max_length=250)
    
