from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.views.generic import CreateView
from django.db import models

from .forms import IncomeForm, ExpenseForm
from .models import Budget

def home(request):
    ''' Home page '''
    return render(request, 'planner/home.html')

def budget_view(request, id_):
    ''' Budget detail by month '''
    budget = get_object_or_404(Budget, pk=id_)
    month = budget.get_month_name()
    planned_expenses = budget.get_planned_expeses()
    planned_incomes = budget.get_planned_incomes()
    context = {'budget': budget, 'month': month,
               'planned_expenses': planned_expenses, 'planned_incomes': planned_incomes}
    return render(request, 'planner/budget.html', context)

def add_expenses_and_incomes(request, id_):
    ''' Add expense or income to a budget '''
    budget = get_object_or_404(Budget, pk=id_)
    incomes = budget.get_actual_incomes()
    expenses = budget.get_actual_expenses()
    total_incomes = Budget.objects.values(
            'incomes__category__name').annotate(models.Sum('incomes__amount'))
    print(total_incomes)
    context = {
        'budget_id': budget.id,
        'incomes': incomes,
        'expenses': expenses
    }
    return render(request, 'planner/add_elements.html', context)

def add_movement_snippet(request):
    if request.method == 'POST':
        clazz = _get_form(request.POST.get('action'))
        print(request.POST.get('action'))
        budget = get_object_or_404(Budget, pk=request.POST.get('id'))
        form = clazz(request.POST)
        if form.is_valid():
            new_mov = form.save(commit=False)
            new_mov.save()
            new_mov.budget_set.add(budget)
            form.save_m2m()
        # TODO: manage error
        print(form.errors)
        print(request.POST)
        return redirect('add', id_=budget.id)
    elif request.is_ajax() and request.method == 'GET':
        clazz = _get_form(request.GET.get('action'))
        form = clazz(auto_id=False)
        html = render_to_string('planner/add_element_snippet.html', {'form': form})
        return HttpResponse(html)
    return HttpResponseNotFound("Page not found")

def _get_form(action):
    return ExpenseForm if action in 'expenses' else IncomeForm

class BudgetCreateView(CreateView):
    model = Budget
    fields = ('month', 'initial_amoumt', 'planned_expense', 'planned_income')
    template_name = 'planner/new_budget.html'
