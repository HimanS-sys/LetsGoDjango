from django.db import models

# Profiles - creates object containing
# user profile details
class Profile(models.Model):
    name = models.CharField(max_length=255)
