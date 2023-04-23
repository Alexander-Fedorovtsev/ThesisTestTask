from rest_framework.routers import DefaultRouter
from django.urls import re_path
from api.views import EmployeeViewSet, DepartmentViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

app_name = 'api'

schema_view = get_schema_view(
    openapi.Info(
        title="API для сотрудников и департаментов",
        default_version='v1',
        description="",
        terms_of_service="https://github.com/Alexander-Fedorovtsev",
        contact=openapi.Contact(email="fedorovtsev@mail.ru"),
        license=openapi.License(name=""),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

router = DefaultRouter()
router.register('employees', EmployeeViewSet, basename='employees')
router.register('departments', DepartmentViewSet, basename='departments')
urlpatterns += router.urls
