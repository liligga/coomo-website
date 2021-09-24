from django.contrib.auth.models import User
from django.db import models


class OneTimePassword(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp = models.IntegerField(default=0)
