"""atlantis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from planner import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('new_budget', views.BudgetCreateView.as_view(), name='new_budget'),
    path('budget/<int:id_>', views.budget_view, name='budget'),
    path('add_movement/budget/<int:id_>', views.add_expenses_and_incomes, name='add'),
    re_path(r'^ajax/get/categories/$', views.get_new_element_form, name='get_cat')
]
