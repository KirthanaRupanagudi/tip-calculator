#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
print("Welcome to the tip calaculator.")
total_bill = input("What was the total bill? $")
tip_per = input("what percentage tip would you like to give? 10, 12 or 15? ")
split_number = input("How many people to split the bill? ")
tip = (int(tip_per)/100)+1
bill =  float(total_bill)*tip
each_pay = bill / int(split_number)
print("${:.2f}".format(each_pay))
