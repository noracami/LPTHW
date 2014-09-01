import random
from sys import exit

__DEBUG__ = not True

#def gold_room()
def is_it_right(choice, number):
    # choice[1, 2, 3, 4]
    # number[5, 6, 3, 2]
    # result[0, B, A, 0]
    
    if __DEBUG__:
        #print("Call is_it_right([0, 0, 0, 0], [0, 0, 0, 0])")
        print("Call is_it_right(%r, %r)" % (choice, number))

    l = len(number)
    result = [0] * l
    c = [x for x in choice]
    n = [x for x in number]
    reply = reply_A(c, n)
    for x in range(l):
        if reply[x] == 1:
            result[x] = 'A'
    
    reply = reply_B(c, n)
    for x in range(l):
        if reply[x] == 1:
            result[x] = 'B'
    #
    print("%d A %d B" % (result.count('A'), result.count('B')))
    if result.count('A') == l:
        return True
    else:
        return False

def reply_A(choice, number):
    reply = [0] * len(number)
    for x in range(min(len(choice), len(number))):
        if choice[x] == number[x]:
            reply[x] = 1
            number[x] = -1
    if __DEBUG__ == True:
        print()
        print("reply_A(%r, %r) = %r" % (choice, number, reply))
        print()
    return reply

def reply_B(choice, number):
    reply = [0] * len(number)
    for x in range(min(len(choice), len(number))):
        for y in range(min(len(choice), len(number))):
            if choice[x] == number[y]:
                reply[x] = 1
                number[y] = -2
    if __DEBUG__ == True:
        print()
        print("reply_B(%r, %r) = %r" % (choice, number, reply))
        print()
    return reply


#def bear_room()
def num_to_list(num):
    output = list(num)
    output = [int(x, 10) for x in output]
#        print("num => %d\ntemp_number => %d" % (num, temp_number))

    return output

#def cthulhu_room()
def input_int_plz(str):
    while True:
        print(str)
        output = input(">>> ")
        if output.isdigit() == True:
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
    if __DEBUG__ == True:
        print(output)
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
    try_again = True
    set_level = False
    level = 4
    
    while try_again == True:
        if set_level == True:
            level = int(input_int_plz("choose how many numbers you want ?"), 10)

        rnd_number = get_random_number(level)
        guess = False
        
        while guess == False:
            choice = input_int_plz("choose a number ;)") # 1234
            choice = num_to_list(choice) # 1234 => [1, 2, 3, 4]
            guess = is_it_right(choice, rnd_number) # ([1, 2, 3, 4], [5, 6, 7, 8])
            
            if guess == True:
                print("would you like to try again ? (yes/N)")
                
                if input(">>> ") == 'yes':
                    # try again
                    try_again = set_level = True
                else:
                    print("Good bye ._./~")
                    try_again = False
        #End while -guess over
    #End while -game over
    exit()

#if __name__ == '__name__':
main()