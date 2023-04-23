from django.http import JsonResponse
from django.shortcuts import render

from company.models import Employee, Department
from company.serializers import EmployeeSerializer, DepartmentSerializer

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination



def employee_list(request):
    if request.user.is_authenticated:
        # Получаем список сотрудников
        employees = Employee.objects.all()
        # Фильтруем по фамилии и по id департамента
        if 'last_name' in request.GET:
            employees = employees.filter(last_name=request.GET['last_name'])
        if 'department_id' in request.GET:
            employees = employees.filter(department_id=request.GET['department_id'])
        # Возвращаем список сотрудников в формате JSON
        return JsonResponse({'employees': list(employees.values())})
    else:
        return JsonResponse({'error': 'You must be authenticated to access this endpoint'}, status=401)

def add_employee(request):
    if request.user.is_authenticated:
        # Получаем данные из запроса
        data = request.POST
        # Создаем нового сотрудника
        employee = Employee.objects.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            department_id=data['department_id']
        )
        # Возвращаем данные о сотруднике в формате JSON
        return JsonResponse({'employee': employee.to_dict()})
    else:
        return JsonResponse({'error': 'You must be authenticated to access this endpoint'}, status=401)

def delete_employee(request):
    if request.user.is_authenticated:
        # Получаем данные из запроса
        data = request.POST
        # Получаем сотрудника по id
        employee = Employee.objects.get(id=data['id'])
        # Удаляем сотрудника
        employee.delete()
        # Возвращаем подтверждение в формате JSON
        return JsonResponse({'message': 'Employee deleted successfully'})
    else:
        return JsonResponse({'error': 'You must be authenticated to access this endpoint'}, status=401)

def department_list(request):
    # Получаем список департаментов
    departments = Department.objects.all()
    # Добавляем искусственное поле с числом сотрудников
    for department in departments:
        department.num_employees = department.employees.count()
        # Добавляем поле с суммарным окладам по всем сотрудникам
        department.total_salary = sum([employee.salary for employee in department.employees.all()])
    # Возвращаем



class EmployeeListView(LoginRequiredMixin, ListView):
    model = Employee
    template_name = 'employee_list.html'
    context_object_name = 'employees'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        last_name = self.request.GET.get('last_name', None)
        department_id = self.request.GET.get('department_id', None)
        if last_name:
            queryset = queryset.filter(last_name__icontains=last_name)
        if department_id:
            queryset = queryset.filter(department_id=department_id)
        return queryset

class DepartmentListView(ListView):
    model = Department
    template_name = 'department_list.html'
    context_object_name = 'departments'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_salary'] = sum(d.total_salary for d in context['departments'])
        return context

urls.py

from django.urls import path
from .views import EmployeeListView, DepartmentListView

urlpatterns = [
    path('employees/', EmployeeListView.as_view(), name='employee_list'),
    path('departments/', DepartmentListView.as_view(), name='department_list'),
]





class EmployeeListView(APIView):
    def get(self, request):
        last_name = request.query_params.get('last_name', None)
        department_id = request.query_params.get('department_id', None)
        employees = Employee.objects.all()
        if last_name is not None:
            employees = employees.filter(last_name=last_name)
        if department_id is not None:
            employees = employees.filter(department_id=department_id)
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    




class EmployeeView(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        employee = Employee.objects.get(pk=pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class DepartmentListView(APIView):
    def get(self, request):
        departments = Department.objects.all()
        data = []
        for department in departments:
            data.append({
                'name': department.name,
                'employees_count': department.employees_count,
                'total_salary': department.total_salary
            })
        return Response(data)
    


class EmployeeListView(APIView):
    pagination_class = PageNumberPagination

    def get(self, request):
        employees = Employee.objects.all()
        paginator = self.pagination_class()
        results = paginator.paginate_queryset(employees, request)
        serializer = EmployeeSerializer(results, many=True)
        return paginator.get_paginated_response(serializer.data)

class DepartmentListView(APIView):
    def get(self, request):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)