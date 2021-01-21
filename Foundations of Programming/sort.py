# William Ikenna-Nwosu (wiknwo)
# 
# Return an array that contains the sorted values from the 
# input array with duplicates removed.
#
# sort([]) → []
# sort([1]) → [1]
# sort([1, 1]) → [1]
def sort(somelist):
    return list(set(somelist))

def main():
    mylist = input("Enter list of numbers separated by single space: ").split(" ")
    mylist = list(mylist)
    print(mylist)
    # Convert list to integers
    for i in range(0, len(mylist)):
        mylist[i] = int(mylist[i])
    print(sort(mylist))

if __name__ == '__main__':
    main()
