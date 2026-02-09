from django.db import models

# Create your models here.
class services(models.Model):
    service_icon=models.CharField(max_length=50)
    service_title=models.CharField(max_length=50)
    service_dis=models.TextField()
