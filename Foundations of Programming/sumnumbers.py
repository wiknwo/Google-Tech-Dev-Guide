# William Ikenna-Nwosu (wiknwo)
#
# SumNumbers
#
# Given a string, return the sum of the numbers appearing in 
# the string, ignoring all other characters. A number is a 
# series of 1 or more digit chars in a row. 
# (Note: Character.isDigit(char) tests if a char is one of 
# the chars '0', '1', .. '9'. Integer.parseInt(string) 
# converts a string to an int.)
#
# sumNumbers("abc123xyz") → 123
# sumNumbers("aa11b33") → 44
# sumNumbers("7 11") → 18
def sumnumbers(somestring):
    sum = 0 # running sum
    value_string = ' # String to hold digits
    for i in range(0, len(somestring)):
        character = somestring[i]

        # Character is a digit and it is last character in string
        if character.isdigit() and (i == len(somestring) - 1):
            value_string = value_string + character
            sum = sum + int(value_string)
            value_string = ""

        # Character is a digit
        elif character.isdigit():
            value_string = value_string + character

        # Character is not digit and value string is empty
        elif (not character.isdigit()) and value_string:
            sum = sum + 0

        # Character is not digit and value string is not empty
        elif (not character.isdigit()) and (not value_string):
            sum = sum + int(value_string)
            value_string = ""
    return sum

def main():
    print(sumnumbers(input("Enter string of alphanumeric and special characters: ")))

if __name__ == '__main__':
    main()