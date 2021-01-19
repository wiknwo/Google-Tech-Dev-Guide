# William Ikenna-Nwosu (wiknwo)
# 
# Given two strings, base and remove, return a version of 
# the base string where all instances of the remove string 
# have been removed (not case sensitive). You may assume that 
# the remove string is length 1 or more. Remove only 
# non-overlapping instances, so with "xxx" removing "xx" 
# leaves "x".
#
# withoutString("Hello there", "llo") → "He there"
# withoutString("Hello there", "e") → "Hllo thr"
# withoutString("Hello there", "x") → "Hello there"
import re

def withoutString(base, remove):
    #remove.tolowercase
    #base.replace(remove, "")
    #newbase = re.compile(base, re.IGNORECASE)
    #newbase_replaced = newbase.sub(remove, "")
    #return newbase_replaced
    return re.sub("(?i){}".format(remove), "", base) #'bye bye bye'


def main():
    base_string = input("Enter base string: ")
    remove_string = input("Enter string to remove from base: ")
    print(withoutString(base_string, remove_string))

if __name__ == '__main__':
    main()