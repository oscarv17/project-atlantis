-- SQLite
SELECT "planner_budget_incomes"."income_id" FROM "planner_budget" LEFT JOIN "planner_budget_incomes" ON ("planner_budget"."id" = "planner_budget_incomes"."budget_id")

