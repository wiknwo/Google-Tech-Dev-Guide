# William Ikenna-Nwosu (wiknwo)
#
# interpret
#
# Write a simple interpreter which understands "+", "-", 
# and "*" operations. Apply the operations in order using 
# command/arg pairs starting with the initial value of 
# "value". If you encounter an unknown command, return -1.
#
# interpret(1, ["+"], [1]) → 2
# interpret(4, ["-"], [2]) → 2
# interpret(1, ["+", "*"], [1, 3]) → 6
def interpret(value, commands, arguments):
    finalvalue = value

    # Processing tokens
    for i in range(0, len(arguments)):
        if commands[i] == "+":
            finalvalue = finalvalue + arguments[i]
        elif commands[i] == "-":
            finalvalue = finalvalue - arguments[i]
        elif commands[i] == "*":
            finalvalue = finalvalue * arguments[i]
        else:
            return -1

    return finalvalue

def main():
    print(interpret(1, ["+", "*"], [1, 3]))

if __name__ == '__main__':
    main()