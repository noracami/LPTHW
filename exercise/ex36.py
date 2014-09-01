from sys import exit

#def gold_room()

#def bear_room()
def num_to_list(num):
    output = []
    temp_number = num

    while temp_number != 0:
        num = temp_number % 10
        output += [num]
        temp_number //= 10

    return output

#def cthulhu_room()
def input_int_plz(str):
    while true:
        print(str)
        output = input(">>> ")
        if output.isdigit() == true:
            return output
        else:
            print("It's not a number :( \n")

#def dead(why)
def get_random_number(level):
    numbers = list(range(10)) # = [x for x in range(10)]
    random.shuffle(numbers)
    output = []
    for x in range(level):
        output += numbers[0::-1]
        del numbers[0::-1]
    return output

def main():
    # welcome messages
    # while-loop:
        # hint user to guess number
        # compare
        # if same:
            # ask for again or quit
        # else:
            # print "1 A 2 B"
    try_again, set_level, level = true, false, 4
    
    while try_again == true:
        if set_level == true:
            level = input_int_plz("choose how many numbers you want ?")

        number = get_random_number(level)
        guess = false
        
        while guess == false:
            choice = input_int_plz("choose a number ;)")
            guess = is_it_right(choice, number) # (1234, [5, 6, 7, 8])
            
            if guess == true:
                print("would you like to try again ? (yes/N)")
                
                if input(">>> ") == 'yes':
                    # try again
                    try_again = set_level = true
                else:
                    print("Good bye ._./~")
        
        #End while -guess over

    #End while -game over

if __name__ == '__name__':
    main()