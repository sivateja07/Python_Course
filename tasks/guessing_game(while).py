#task is to guess a number which is pre set and it has to run it until it is correct but has only 3 chances

sec_num = 8
guess_count = 0
guess_limit = 3

while guess_count < guess_limit: #as long as this is true the loop gets incremented
    guess = int(input("Guess: "))
    guess_count += 1             
    if guess == sec_num:
        print("You won!")
        break                   #breaks the loop and comes outside be careful with indentention
else:                           #similiar to that of a if a while loop also has an else part so it gets executed after the loop 
    print("You failed mate!")