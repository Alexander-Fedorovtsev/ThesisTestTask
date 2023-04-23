from django.contrib import admin

from .models import Employee, Department

from django.utils.safestring import mark_safe


@admin.register(Employee)
class Employee(admin.ModelAdmin):
    list_display = ('name', 'position', 'salary', 'age', 'photo')
    autocomplete_fields = ('department',)
    search_fields = ('name', 'position')
    list_filter = ('department',)
    readonly_fields = ('preview',)

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.photo.url}">')

    preview.short_description = 'Фотография (превью)'


@admin.register(Department)
class Department(admin.ModelAdmin):
    list_display = ('name', 'director')
    search_fields = ('name', 'director')

