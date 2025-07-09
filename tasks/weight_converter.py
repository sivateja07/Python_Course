#The task is to ask the user for his weight and confirm if it's in kgs or lbs (case indepenedent) and convert it to opposite 

weight = input("what is your weight? ")
cnf = input("Is that in kgs (k) or lbs (l)? ")

if cnf.upper() == "K":
    nn = int(weight)*2.2
    print(f"your weight in lbs is : {nn}")
elif cnf.upper() == "L":
    nn = int(weight)*0.45
    print(f"your weight in kgs is : {nn}")
