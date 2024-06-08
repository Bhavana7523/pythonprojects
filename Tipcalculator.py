print("Welcome to the tip calculator")
bill=float(input("What was the total bill?\n"))
tip=int(input("How much tip percentage would you likr to give 10,12 or 15 \n"))
persons=int(input("How many persons do you want to split the bill"))
tip_as_percent=tip/100
total_tip_amount=bill*tip_as_percent
total_bill=bill+total_tip_amount
bill_per_person=total_bill/persons
final_amount=round(bill_per_person,2)
print(f"Each person should pay {final_amount}")

