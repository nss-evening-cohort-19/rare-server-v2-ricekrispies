from django.db import models

class Demotion(models.Model):
    action = models.CharField(max_length=25)
    admin = models.ForeignKey("RareUser", on_delete=models.CASCADE)
    approval = models.ForeignKey("RareUser", on_delete=models.CASCADE)
    modified_user = models.ForeignKey("RareUser", on_delete=models.CASCADE)
