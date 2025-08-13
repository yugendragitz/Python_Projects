print("Welcome to the YUGI'S TIP CALCULATOR!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15"))
people = int(input("How many peoplpe should split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_bill = round(bill_per_person, 2)
print(f"Your total bill is ${final_bill}")