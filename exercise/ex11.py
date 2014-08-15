print ("How old are you?", end = " ")
age = input() # raw_input() was renamed to input() since python3
print ("How tall are you?", end = " ")
height = input()
print ("How much do you weight?", end = " ")
weight = input()

print ("So, you're %r old, %r tall and %r heavy." % (age, height, weight))

x = input(">>> Another Inpt: ")
print (x)