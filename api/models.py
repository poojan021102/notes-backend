from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Note(models.Model):
    user_name = models.ForeignKey(User,on_delete=models.CASCADE)
    note = models.TextField(null=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(null=True,max_length=100)

