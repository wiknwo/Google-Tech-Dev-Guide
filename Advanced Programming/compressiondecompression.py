# William Ikenna-Nwosu (wiknwo)
# 
# Former Coding Interview Question: Compression and 
# Decompression
# 
# In this exercise, you're going to decompress a compressed 
# string. Your input is a compressed string of the format 
# number[string] and the decompressed output form should be 
# the string written number times. For example: The input
# 3[abc]4[ab]c Would be output as abcabcabcababababc
# 
# - Number can have more than one digit. For example, 
#   10[a] is allowed, and just means aaaaaaaaaa
#
# - One repetition can occur inside another. For example, 
#   2[3[a]b] decompresses into aaabaaab
#
# - Characters allowed as input include digits, small 
#   English letters and brackets [ ]. 
# 
# - Digits are only to represent amount of repetitions.
#
# - Letters are just letters.
#
# - Brackets are only part of syntax of writing repeated 
#   substring.
#
# - Input is always valid, so no need to check its validity.
def main():
    stringtodecompress = input("Enter compressed string: ")
    print(stringtodecompress) # Check input read correctly
    valuestring = '' # String to hold digit representing number of times to repeat following string in decompressed string
    decompressedstring = '' # Decompressed string
    repetitions = 0 # Number of times to concatenate inner string
    word = '' # String to hold current word
    
    # Parse the input string
    for character in stringtodecompress:
        if character.isdigit():
            valuestring = valuestring + character
            print("valuestring: {}".format(valuestring))

        elif character.isalpha() and valuestring:
            word = word + character
            print(word)

        # Start of new string
        elif character == "[":
            print("valuestring: {}".format(valuestring))
            repetitions = repetitions + int(valuestring)
            
        # End of new string
        elif character == "]":
            for i in range(0, repetitions):
                decompressedstring = decompressedstring + word
            valuestring = ""
            word = ""
            repetitions = 0

        elif character.isalpha() and not valuestring:
            word = word + character
            decompressedstring = decompressedstring + word
    
    print(decompressedstring)

if __name__ == '__main__':
    main()
