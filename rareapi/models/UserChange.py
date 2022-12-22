from django.db import models

class UserChange(models.Model):
    action = models.CharField(max_length=25)
    admin = models.ForeignKey("RareUser", on_delete=models.CASCADE, related_name='admin')
    second_admin = models.ForeignKey(
        "RareUser", on_delete=models.CASCADE, related_name='second_admin', null=True, default=None)
    modified_user = models.ForeignKey("RareUser", on_delete=models.CASCADE, related_name='modified_user')
