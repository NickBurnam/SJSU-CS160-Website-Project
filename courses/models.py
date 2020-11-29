from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    # fields for the course table.
    name = models.CharField(max_length=800)
    creator = models.CharField(max_length=800)
    description = models.TextField(max_length=5000)
    last_updated_date = models.DateField() 
    average_rating = models.FloatField()
    image = models.URLField(default=None,null=True)

    def __str__(self):
        return self.name 
    
    def __unicode(self):
        return self.name

class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.user.username
