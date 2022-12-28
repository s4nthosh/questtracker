from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    is_teamleader = models.BooleanField('Is teamleader',default=False)
    is_manager = models.BooleanField('Is manager', default=False)
    is_employer = models.BooleanField('Is employer', default=False)


class filesend(models.Model):
    Category = (('manager', 'manager'), ('employer', 'employer'))
    Status = (('Pending', 'Pending'), ('On-progress', 'On-progress'), ('Complete', 'Complete'))

    Name = models.CharField(max_length=20, null=True)
    Designation = models.CharField(max_length=50, null=True)
    Files = models.FileField()
    Department = models.CharField(max_length=200, null=True, choices=Category)
    Status = models.CharField(max_length=200, null=True, choices=Status)


def __str__(self):
    return self.Name
