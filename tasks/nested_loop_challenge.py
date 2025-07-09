#the challenge is to print the times of characters in the list but dont do it like charcter*item, this one is bit tricky
list = [7,5,3,1]
for count in list:
    output = ""
    for u in range(count):
        output += 'x'
    print(output)