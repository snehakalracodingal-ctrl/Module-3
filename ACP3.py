def due_amount(total_bill, amount_paid):
    due = total_bill - amount_paid
    return due

bill = float(input("Enter total bill amount: "))
paid = float(input("Enter amount paid: "))

due = due_amount(bill, paid)

if due > 0:
    print("Customer due amount is:", due)
elif due == 0:
    print("No due amount. Bill cleared.")
else:
    print("Extra amount paid:", abs(due))
