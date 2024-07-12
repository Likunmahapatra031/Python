print("Welcome to the tip calculater")
bill=float(input("What was the total bill? "))
tip=int(input("How much tip would you like to pay?10%,12%,or15?"))
people=int(input("how many people to split the bill?"))
tip_persenentage=tip/100
total_tip_amount=bill*tip_persenentage
total_bill=bill+total_tip_amount
bill_per_person=total_bill/people
final_amount= round(bill_per_person,2)
print(f"each person should pay{final_amount}")


