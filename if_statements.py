#work like conditions
#example implementation

is_hot = False
is_cold = False
if is_hot:
    print("It's a hot day") #if True this part will be executed

if is_cold:
    print("It's a cold day") #if Ture this part will be executed
else:
    print("It's a beautiful day") #Neither this will be executed
print("enjoy your day mate!")


#task 
price = 1000000
good_credit = True

if good_credit:
    x = 0.1*price
else:
    x = 0.2*price
print(f"downpayement is: $ {x}")