#one valuable lesson learnt called DRY - Don't Repeat yourself which is not to use the same repeatedly like using an operator many times
#in simple terms do not duplicate it a lot

command = ""   #initialisation with an empty string 

while True:  #saying this loop will run until we excplicitly mention to break out of it 
    command = input("> ").lower()
    if command == "help":
        print(''' 
start - to start the car
stop  - to stop the car
quit - to exit the program''')  #what ever inside a print statement will be printed including the indentention
    elif command == "start":
        print("engine started, off we go...")
    elif command == "stop":
        print("Engine haulted!")
    elif command == "quit":            #elif is else if , remember if and elif are different implementations
        break
    else:
        print("sorry bud, I don't understand")