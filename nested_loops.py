#nested loops implementation for co-ordinates like in the form of x and y
for x in range(5): #in first iteration x holds 0
    for u in range(3):
        print(f'({x}, {u})')   #program flow is like x still holding 0 u holds 0 and then returns x,u but it will first complete the 
                               # inner u loop and then go to x loop like this and so on.....