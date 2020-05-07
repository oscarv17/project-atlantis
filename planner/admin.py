from django.contrib import admin

from .models import PlannedIncome, PlannedExpense, Category

admin.site.register(Category)
admin.site.register(PlannedExpense)
admin.site.register(PlannedIncome)
