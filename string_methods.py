char = "This is a sample line just to test"
print(len(char)) #returns the length of the string#
print(char.upper())
print(char) #this wont make a change as . operator works only on that paricular line#
print(char.find('b')) #returns -1 means not exists
print(char.find('ample'))
print(char.replace('test', 'implement'))
print(char) #see it will still return the default

print("This" in char)