from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField()
    position = models.CharField(max_length=100)
    salary = models.FloatField()
    age = models.IntegerField()
    department = models.ForeignKey('Department', related_name='employees', on_delete=models.CASCADE)


class Department(models.Model):
    name = models.CharField(max_length=255)
    director = models.ForeignKey(Employee, related_name='mydepartment', on_delete=models.CASCADE)
