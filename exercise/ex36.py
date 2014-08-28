from sys import exit

#def gold_room()

#def bear_room()

#def cthulhu_room()

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
    set_level, level = false, 4
    if set_level == true:
        print("choice how many numbers you want")
        level = input(">>> ") #str.isdigit()


    number = get_random_number(level)
    guess = false
    while guess == false:
        print("your choice ;)")
        choice = input(">>> ")
        if choice.isdigit():
            pass
        else:
            exit()

if __name__ == '__name__':
    main()