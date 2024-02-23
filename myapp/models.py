from django.db import models

# Profiles - creates object containing
# user profile details
class Profile(models.Model):
    name = models.CharField(max_length=255, unique=True)
    mobile_number = models.CharField(max_length=10)
    address = models.TextField()
    email = models.EmailField(max_length=320)
