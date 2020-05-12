from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from .models import Income, Expense

class IncomeForm(ModelForm):
    class Meta:
        model = Income
        fields = ['income_date', 'amount', 'description', 'category']
        labels = {
            'income_date' : _(''),
            'amount' : _(''),
            'description' : _(''),
            'category' : _(''),
        }