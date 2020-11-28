def total_expenses(expenses):
    total = 0
    for expense in expenses:
        total += expense["expense"]
    return total