from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.views.generic import CreateView

from .forms import IncomeForm, ExpenseForm
from .models import Budget

def home(request):
    ''' Home page '''
    budgets = Budget.objects.all()
    return render(request, 'planner/home.html', {'budgets': budgets})

def budget_view(request, id_):
    ''' Budget detail by month '''
    budget = get_object_or_404(Budget, pk=id_)

    month = budget.get_month_name()
    planned_expenses = budget.get_planned_expeses()
    planned_incomes = budget.get_planned_incomes()
    total_incomes_cat = budget.get_total_incomes_by_category()
    total_expenses_cat = budget.get_total_expenses_by_category()
    total_planned_expenses = budget.get_total_planned_expenses()
    total_planned_incomes = budget.get_total_planned_incomes()
    total_incomes = sum(total_incomes_cat.values())
    total_expenses = sum(total_expenses_cat.values())

    context = {'budget': budget, 'month': month,
               'planned_expenses': planned_expenses,
               'planned_incomes': planned_incomes,
               'total_incomes_cat': total_incomes_cat,
               'total_expenses_cat': total_expenses_cat,
               'total_planned_in': total_planned_incomes['amount'],
               'total_planned_ex': total_planned_expenses['amount'],
               'total_incomes': total_incomes,
               'total_expenses': total_expenses
               }

    return render(request, 'planner/budget.html', context)

def add_expenses_and_incomes(request, id_):
    ''' Add expense or income to a budget '''
    budget = get_object_or_404(Budget, pk=id_)
    incomes = budget.get_actual_incomes()
    expenses = budget.get_actual_expenses()
    context = {
        'budget_id': budget.id,
        'incomes': incomes,
        'expenses': expenses
    }
    return render(request, 'planner/add_elements.html', context)

def add_movement_snippet(request):
    ''' Return the form for the income/expenses tables '''
    if request.method == 'POST':
        clazz = _get_form(request.POST.get('action'))
        print(request.POST.get('edit-id'))
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
    ''' Create budget view '''
    model = Budget
    fields = ('month', 'initial_amoumt', 'planned_expense', 'planned_income')
    template_name = 'planner/new_budget.html'
