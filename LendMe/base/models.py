from django.db import models

# Create your models here.  

class LendMe(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    credit_score = models.PositiveIntegerField()
    annual_income = models.DecimalField(max_digits=10, decimal_places=2) 
    pan_card = models.CharField(max_length=15)