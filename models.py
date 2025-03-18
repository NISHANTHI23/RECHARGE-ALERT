from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    recharge_plan_validity = models.DateField()

    def __str__(self):
        return self.name
