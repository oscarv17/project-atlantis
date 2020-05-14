from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.views.generic import CreateView

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
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():

            new_mov = form.save(commit=False)
            new_mov.save()
            budget = get_object_or_404(Budget, pk=request.POST.get('id'))
            new_mov.budget_set.add(budget)
            form.save_m2m()

    budget = get_object_or_404(Budget, pk=id_)
    incomes = budget.get_actual_incomes()
    expenses = budget.get_actual_expenses()
    context = {
        'budget_id': budget.id,
        'incomes': incomes,
        'expenses': expenses
    }
    return render(request, 'planner/add_elements.html', context)

def get_new_element_form(request):
    form = ExpenseForm(auto_id=False) if request.GET.get('action') == 'expenses' else IncomeForm(auto_id=False)
    if request.is_ajax() and request.method == 'GET':
        html = render_to_string('planner/add_element_snippet.html', {'form': form})
        return HttpResponse(html)
    elif request.method == 'POST':
        print(request.POST)
    return HttpResponseNotFound("Page not found")

class BudgetCreateView(CreateView):
    model = Budget
    fields = ('month', 'initial_amoumt', 'planned_expense', 'planned_income')
    template_name = 'planner/new_budget.html'
