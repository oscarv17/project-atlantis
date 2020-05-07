# Generated by Django 3.0.6 on 2020-05-07 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('category_type', models.CharField(choices=[('ex', 'expense'), ('in', 'income')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PlannedIncome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planned_amount', models.FloatField()),
                ('actual_amount', models.FloatField(default=0.0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.Category')),
            ],
        ),
        migrations.CreateModel(
            name='PlannedExpense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planned_amount', models.FloatField()),
                ('actual_amount', models.FloatField(default=0.0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income_date', models.DateField()),
                ('amount', models.FloatField()),
                ('description', models.CharField(max_length=250)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expense_date', models.DateField()),
                ('amount', models.FloatField()),
                ('description', models.CharField(max_length=250)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.IntegerField()),
                ('initial_amoumt', models.FloatField()),
                ('expenses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.Expense')),
                ('incomes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.Income')),
            ],
        ),
    ]