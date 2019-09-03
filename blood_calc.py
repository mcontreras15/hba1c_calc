#user input for blood glucose (eAg) in mg/dL
eAg = int(input("Enter eAg mg/dL: "))

#HbA1C is calculated by using the formula 28.7 x HbA1C - 46.7 = eAg 
hba1c = (eAg + 46.7) /28.7

#we need to round the output to 2 decimal places
output = round(hba1c,2)
print("You HbA1C is",output,"today.")
