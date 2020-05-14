from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Income, Expense, Category

class IncomeForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.get_category_in(), label='')

    class Meta:
        model = Income
        fields = ['income_date', 'amount', 'description', 'category']
        labels = {
            'income_date' : _(''),
            'amount' : _(''),
            'description' : _('')
        }
        widgets = {
            'income_date': forms.DateInput(attrs={'placeholder': 'Fecha', 'class': 'datepicker'}),
            'amount': forms.NumberInput(attrs={'placeholder': 'Monto'}),
            'description': forms.TextInput(attrs={'placeholder': 'Descripcion'})
        }


class ExpenseForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.get_category_ex(), label='')

    class Meta:
        model = Expense
        fields = ['expense_date', 'amount', 'description', 'category']
        labels = {
            'expense_date' : _(''),
            'amount' : _(''),
            'description' : _('')
        }
        widgets = {
            'expense_date': forms.DateInput(attrs={'placeholder': 'Fecha', 'class': 'datepicker'}),
            'amount': forms.NumberInput(attrs={'placeholder': 'Monto'}),
            'description': forms.TextInput(attrs={'placeholder': 'Descripcion'})
        }
