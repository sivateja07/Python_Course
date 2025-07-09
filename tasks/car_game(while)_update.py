command = ""   #initialisation with an empty string 
started = False #a boolean set to store the condition of car
while True:  #saying this loop will run until we excplicitly mention to break out of it 
    command = input("> ").lower()
    if command == "help":
        print(''' 
start - to start the car
stop  - to stop the car
quit - to exit the program''')  #what ever inside a print statement will be printed including the indentention
    elif command == "start":
        if started:
            print("Engine already started mate...!")
        else: 
            started = True #turn on , means start to true 
            print("engine started, off we go...")
    elif command == "stop":
        if not started: #used not so started will become True 
            print("engine already stopped bro")
        else:
            started = False
            print("Engine haulted!")
    elif command == "quit":            #elif is else if , remember if and elif are different implementations
        break
    else:
        print("sorry bud, I don't understand")