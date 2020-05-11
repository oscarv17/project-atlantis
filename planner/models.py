from django.db import models
from django.shortcuts import reverse

MONTHS = {
        1: 'Enero',
        2: 'Febrero',
        3: 'Marzo',
        4: 'Abril',
        5: 'Mayo',
        6: 'Junio',
        7: 'Julio',
        8: 'Agosto',
        9: 'Septiembre',
        10: 'Octubre',
        11: 'Noviembre',
        12: 'Diciembre'
    }

class CategoryQuerySet(models.QuerySet):
    def get_category_in(self):
        return self.filter(category_type='in').values_list('name', flat=True)

    def get_category_ex(self):
        return self.filter(category_type='ex').values_list('name', flat=True)

class Category(models.Model):
    types = [
        ('ex', 'expense'),
        ('in', 'income')
    ]
    name = models.CharField(max_length=250)
    category_type = models.CharField(max_length=50, choices=types)

    objects = CategoryQuerySet.as_manager()

    def __str__(self):
        return f'Category: {self.name}, type: {self.category_type}'

class PlannedIncome(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    planned_amount = models.FloatField()
    actual_amount = models.FloatField(default=0.0)

    def __str__(self):
        return f'{self.category.name} expected: {self.planned_amount}'

class PlannedExpense(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    planned_amount = models.FloatField()
    actual_amount = models.FloatField(default=0.0)

    def __str__(self):
        return f'{self.category.name} expected: {self.planned_amount}'
            
class Expense(models.Model):
    expense_date = models.DateField()
    amount = models.FloatField()
    description = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Income(models.Model):
    income_date = models.DateField()
    amount = models.FloatField()
    description = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Budget(models.Model):
    expenses = models.ManyToManyField(Expense)
    incomes = models.ManyToManyField(Income)
    planned_income = models.ManyToManyField(PlannedIncome)
    planned_expense = models.ManyToManyField(PlannedExpense)
    month = models.IntegerField()
    initial_amoumt = models.FloatField()

    def get_month_name(self):
        return MONTHS.get(self.month)
    
    def get_planned_expeses(self):
        return self.planned_expense.all()

    def get_planned_incomes(self):
        return self.planned_income.all()

    def get_absolute_url(self):
        return reverse('budget', args=[self.id])