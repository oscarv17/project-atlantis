from django.core import serializers
from django.http import HttpResponseNotFound, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView

from .models import Budget, Category

def home(request):
    return render(request, 'planner/home.html')

def budget_view(request, id):
    budget = get_object_or_404(Budget, pk=id)
    month = budget.get_month_name()
    planned_expenses = budget.get_planned_expeses()
    planned_incomes = budget.get_planned_incomes()
    context = {'budget': budget, 'month': month, 
               'planned_expenses': planned_expenses, 'planned_incomes': planned_incomes}
    return render(request, 'planner/budget.html', context)

def add_expenses_and_incomes(request):
    return render(request, 'planner/add_elements.html')

def get_categories(request):
    if request.is_ajax and request.method == 'GET':
        action = request.GET.get('action')
        if action == 'expenses':
            data = Category.objects.get_category_ex()
        else:
            data = Category.objects.get_category_in()
        # serialized_data = serializers.serialize('json', data)
        return JsonResponse({'categories': list(data)})
    return HttpResponseNotFound("Page not found")

class BudgetCreateView(CreateView):
    model = Budget
    fields = ('month', 'initial_amoumt', 'planned_expense', 'planned_income')
    template_name = 'planner/new_budget.html'
