from django.db.models import Sum, Count
from company.models import Employee, Department
from company.serializers import EmployeeSerializer, DepartmentSerializer

from rest_framework import viewsets

from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = EmployeeSerializer
    http_method_names = ['get', 'post', 'delete']
    pagination_class = PageNumberPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name', 'department')


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    http_method_names = ('get',)

    def get_queryset(self):
        return Department.objects.annotate(
            total_employees=Count('employees'),
            sum_salary=Sum('employees__salary')
        )
