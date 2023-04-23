from django.db import models


class Employee(models.Model):
    name = models.CharField('ФИО сотрудника', max_length=100)
    photo = models.ImageField('Фотография')
    position = models.CharField('Должность', max_length=100)
    salary = models.FloatField('Оклад')
    age = models.IntegerField('Возраст')
    department = models.ForeignKey('Department', verbose_name='Департамент', related_name='employees',
                                   on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f'{self.name} - {self.position}'

class Department(models.Model):
    name = models.CharField('Название', max_length=255)
    director = models.ForeignKey(Employee, verbose_name='Директор', related_name='mydepartment', blank=True, null=True,
                                 on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департаменты'

    def __str__(self):
        return f'{self.name}, директор: {self.director.name}'
