name = input("what is your name? ")
year = input('Hi '+name+ ' what is your birthyear? ')
age = 2025 - int(year) # this is the type conversion we convert here string to a integer#
print("Dear "+name+" your age is: ",age) #also a string cannot be concatinated with a numberical (strign)#

new = input("enter a num:")
new_new = int(new)
print(type(new_new)) #type() function used to determine the type of the variable also we have bool(), float()#

#activity#
usr = input("what is your weight (in pounds)? ")
up_usr = float(usr)
weig = up_usr*0.45
usr_weig = print("your weight (in kgs) is ", weig)