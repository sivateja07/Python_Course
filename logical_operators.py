#logical operators are like combining both conditions like if both are true (and), one of them is true (or)

high_income = True
high_credit = True

if high_income and high_credit:
    print("This guy is having a good life")

tall = True
rich = False

if tall or rich:
    print("eligible to be a boyfriend")

#not operator

good = True
history = False

if good and not history:   #not operator changes false to true, ture ot flase so here we used and which has two true statements
    print("good guy")