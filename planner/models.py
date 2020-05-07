from django.db import models

class Category(models.Model):
    types = [
        ('ex', 'expense'),
        ('in', 'income')
    ]
    name = models.CharField(max_length=250)
    category_type = models.CharField(max_length=50,choices=types)

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
    expenses = models.ForeignKey(Expense, on_delete=models.CASCADE)
    incomes = models.ForeignKey(Income, on_delete=models.CASCADE)
    planned_income = models.ManyToManyField(PlannedIncome)
    expense_income = models.ManyToManyField(PlannedExpense)
    month = models.IntegerField()
    initial_amoumt = models.FloatField()