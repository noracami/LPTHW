import random
from sys import exit

__DEBUG__ = True

#def gold_room()
def is_it_right(choice, number):
    # choice[1, 2, 3, 4]
    # number[5, 6, 3, 2]
    # result[0, B, A, 0]
    
    result = ['0'] * 4
    c = choice
    n = number    
    reply = reply_A(c, n)
    for x in range(len(n)):
        if reply[x] == 1:
            result[x] = 'A'
            n[x] = -1
    
    reply = reply_B(c, n)
    for x in range(len(n)):
        if reply[x] == 1:
            result[x] = 'B'
    #
    print("%d A %d B" % (result.count('A'), result.count('B')))
    if result.count('A') == 4:
        return True
    else:
        return False

def reply_A(choice, number):
    reply = [0] * 4
    c = choice
    n = number
    for x in range(len(c)):
        if c[x] == n[x]:
            reply[x] = 1
    if __DEBUG__ == True:
        print()
        print("reply_A(%r, %r) = %r" % (c, n, reply))
        print()
    return reply

def reply_B(choice, number):
    reply = [0] * 4
    c = choice
    n = number
    for x in range(len(c)):
        for y in range(len(c)):
            if c[x] == n[y]:
                reply[x] = 1
                n[y] = -1
    if __DEBUG__ == True:
        print()
        print("reply_B(%r, %r) = %r" % (c, n, reply))
        print()
    return reply


#def bear_room()
def num_to_list(num):
    output = []
    temp_number = num

    while temp_number != 0:
        num = (temp_number % 10)
        output += [num]
        temp_number //= 10
#        print("num => %d\ntemp_number => %d" % (num, temp_number))

    output = output[::-1]

    return output

#def cthulhu_room()
def input_int_plz(str):
    while True:
        print(str)
        output = input(">>> ")
        if output.isdigit() == True:
            return int(output, 10)
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
            level = input_int_plz("choose how many numbers you want ?")

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
        #End while -guess over
    #End while -game over
    exit()

#if __name__ == '__name__':
main()