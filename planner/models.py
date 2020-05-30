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
    ''' Custom QuerySet for Category model '''
    def get_category_in(self):
        ''' Returns all the categories of type income '''
        return self.filter(category_type='in')

    def get_category_ex(self):
        ''' Returns all the categories of type expense '''
        return self.filter(category_type='ex')

class Category(models.Model):
    ''' Model for categories.
        It has a name and a type (income and expense)
    '''
    types = [
        ('ex', 'expense'),
        ('in', 'income')
    ]
    name = models.CharField(max_length=250)
    category_type = models.CharField(max_length=50, choices=types)

    objects = CategoryQuerySet.as_manager()

    def __str__(self):
        return f'{self.name}'

class PlannedIncome(models.Model):
    ''' Model for incomes planned in a month.
        It has a Category asociated,
        a planned amount and the actual amount
    '''
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    planned_amount = models.FloatField()
    actual_amount = models.FloatField(default=0.0)

    def __str__(self):
        return f'{self.category.name} expected: {self.planned_amount}'

class PlannedExpense(models.Model):
    ''' Model for expenses planned in a month.
        It has a Category asociated,
        a planned amount and the actual amount
    '''
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    planned_amount = models.FloatField()
    actual_amount = models.FloatField(default=0.0)

    def __str__(self):
        return f'{self.category.name} expected: {self.planned_amount}'

class Expense(models.Model):
    ''' Model for expense made in a month.
        It has a date when happenned,
        an amount, the description and
        a category associated
    '''
    expense_date = models.DateField()
    amount = models.FloatField()
    description = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Income(models.Model):
    ''' Model for expense made in a month.
        It has a date when happenned,
        an amount, the description and
        a category associated
    '''
    income_date = models.DateField()
    amount = models.FloatField()
    description = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Budget(models.Model):
    ''' Model for a budget for a month.
        It has a expense, income, planned income,
        planned expnese associated, the month of the
        budget and an initial amount
    '''
    expenses = models.ManyToManyField(Expense)
    incomes = models.ManyToManyField(Income)
    planned_income = models.ManyToManyField(PlannedIncome)
    planned_expense = models.ManyToManyField(PlannedExpense)
    month = models.IntegerField()
    initial_amoumt = models.FloatField()

    def get_month_name(self):
        ''' Returns the month of the budget as name '''
        return MONTHS.get(self.month)

    def get_planned_expeses(self):
        ''' Returns all the planned expenses of a budget '''
        return self.planned_expense.all()

    def get_planned_incomes(self):
        ''' Returns all the planned incomes of a budget '''
        return self.planned_income.all()

    def get_actual_expenses(self):
        ''' Returns all the actual expenses of a budget '''
        return self.expenses.all()

    def get_actual_incomes(self):
        ''' Returns all the actual incomes of a budget '''
        return self.incomes.all()

    def get_absolute_url(self):
        ''' Returns the url associated with the budget '''
        return reverse('budget', args=[self.id])

    def get_total_incomes_by_category(self):
        ''' Returns the total amount incomes grouped by categories '''
        totals = self.incomes.all().values(
            category_name=models.F('category__name')).annotate(
                amount=models.Sum('amount'))

        return {val['category_name']: val['amount'] for val in totals}

    def get_total_expenses_by_category(self):
        ''' Returns the total amount expenses grouped by categories '''
        totals = self.expenses.all().values(
            category_name=models.F('category__name')).annotate(
                amount=models.Sum('amount'))

        return {val['category_name']: val['amount'] for val in totals}

    def get_total_planned_incomes(self):
        ''' Returns the total amount of planned incomes '''
        return self.planned_income.all().aggregate(
            amount=models.Sum('planned_amount'))

    def get_total_planned_expenses(self):
        ''' Returns the total amount of planned expenses '''
        return self.planned_expense.all().aggregate(
            amount=models.Sum('planned_amount'))
 