from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view



schema_view = get_swagger_view(title="Swagger Docs")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title='My API title')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
