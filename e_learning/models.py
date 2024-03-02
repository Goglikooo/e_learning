from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    category = models.CharField(max_length=35)
    url = models.TextField(default="https://freedesignfile.com/upload/2022/10/Young-people-learning-English-illustration-vector.jpg")



class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)
    


