# William Ikenna-Nwosu (wiknwo)
#
# Given an array of strings, return a Map<String, Integer> 
# containing a key for every different string in the array, 
# always with the value 0. For example the string "hello" 
# makes the pair "hello":0. We'll do more complicated 
# counting later, but for this problem the value is simply 0.
# 
# word0(["a", "b", "a", "b"]) → {"a": 0, "b": 0}
# word0(["a", "b", "a", "c", "b"]) → {"a": 0, "b": 0, "c": 0}
# word0(["c", "b", "a"]) → {"a": 0, "b": 0, "c": 0}
def wordzero(somestrings):
    my_dict = {}

    # Make the map
    for i in range(0, len(somestrings)):
        my_dict[somestrings[i]] = 0
    
    return my_dict

def main():
    letters = input("Enter comma separated list of letters: ").split(" ")
    print(letters)
    print(wordzero(letters))

if __name__ == '_main__':
    main()