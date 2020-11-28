from django.db import models
from mainApp.models import Page
from django.contrib.auth.models import User

# Create your models here.

class Notification(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    last_notified = models.DateTimeField()    
