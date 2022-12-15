from django.db import models

class Demotion(models.Model):
    action = models.CharField(max_length=25)
    admin = models.ForeignKey("RareUser", on_delete=models.CASCADE, related_name='admin')
    approval = models.ForeignKey("RareUser", on_delete=models.CASCADE, related_name='approval')
    modified_user = models.ForeignKey("RareUser", on_delete=models.CASCADE, related_name='modified_user')
