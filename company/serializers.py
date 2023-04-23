from rest_framework import serializers
from .models import Employee, Department


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('pk', 'name', 'photo', 'position', 'salary', 'age', 'department')


class DepartmentSerializer(serializers.ModelSerializer):
    total_employees = serializers.IntegerField()
    sum_salary = serializers.FloatField()

    class Meta:
        model = Department
        fields = ('name', 'director', 'total_employees', 'sum_salary')
