from django.db import models
from django.contrib.auth.models import User


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default="", blank=True)
    website = models.CharField(max_length=250)
    is_responded = models.BooleanField(default=False, blank=True)
    is_negative = models.BooleanField(default=False, blank=True)
    additional_info = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
