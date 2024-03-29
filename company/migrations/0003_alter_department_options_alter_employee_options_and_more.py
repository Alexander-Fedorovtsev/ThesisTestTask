# Generated by Django 4.2 on 2023-04-23 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_alter_department_director'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name': 'Департамент', 'verbose_name_plural': 'Департаменты'},
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'Сотрудник', 'verbose_name_plural': 'Сотрудники'},
        ),
        migrations.AlterField(
            model_name='department',
            name='director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mydepartment', to='company.employee', verbose_name='Директор'),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='age',
            field=models.IntegerField(verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='company.department', verbose_name='Департамент'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='ФИО сотрудника'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(upload_to='', verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(max_length=100, verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.FloatField(verbose_name='Оклад'),
        ),
    ]
