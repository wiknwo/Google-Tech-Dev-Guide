# William Ikenna-Nwosu (wiknwo)
#
# Given an array of strings, return a Map<String, Integer> 
# containing a key for every different string in the array, 
# and the value is that string's length.
# 
# wordLen(["a", "bb", "a", "bb"]) → {"bb": 2, "a": 1}
# wordLen(["this", "and", "that", "and"]) → {"that": 4, "and": 3, "this": 4}
# wordLen(["code", "code", "code", "bug"]) → {"code": 4, "bug": 3}
def wordlen(somestrings):
    my_dict = {}

    # Make the map
    for i in range(0, len(somestrings)):
        my_dict[somestrings[i][0]] = somestrings[i][len(somestrings[i]) -1]
    return my_dict

def main():
    letters = input("Enter comma separated list of letters: ").split(" ")
    print(letters)
    print(wordlen(letters))

if __name__ == '_main__':
    main()