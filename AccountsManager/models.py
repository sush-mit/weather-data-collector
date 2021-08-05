from django.db import models

class UserAccountsModel(models.Model):
    user_name = models.CharField(max_length=32)
    user_email = models.CharField(max_length=256)
    user_password = models.CharField(max_length=32)