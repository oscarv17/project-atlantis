from django.shortcuts import render
from django.views.generic import CreateView

from .models import Budget

def home(request):
    return render(request, 'planner/home.html')


class BudgetCreateView(CreateView):
    model = Budget
    fields = ('month', 'initial_amoumt', 'expense_income', 'planned_income')
    template_name = 'planner/new_budget.html'


def new_budget(request):
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

    return render(request, 'planner/new_budget.html', {'months': MONTHS})
