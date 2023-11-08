from django.db import models

# Create your models here.
class StoreData(models.Model):
    Subj = models.CharField(max_length=20)
    Messa = models.CharField(max_length=20)
    Self_email = models.EmailField(max_length=20)
    Customer_email = models.EmailField(max_length=20)