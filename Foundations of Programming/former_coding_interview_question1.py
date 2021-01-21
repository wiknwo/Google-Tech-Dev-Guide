# William Ikenna-Nwosu (wiknwo)
# Given a string S and a set of words D, find the longest 
# word in D that is a subsequence of S.
#
# Word W is a subsequence of S if some number of characters, 
# possibly zero, can be deleted from S to form W, without 
# reordering the remaining characters.
#
# Note: D can appear in any format (list, hash table, prefix 
# tree, etc.
#
# For example, given the input of S = "abppplee" and 
# D = {"able", "ale", "apple", "bale", "kangaroo"} the 
# correct output would be "apple"
#
# - The words "able" and "ale" are both subsequences of S, 
#   but they are shorter than "apple".
#
# - The word "bale" is not a subsequence of S because even 
#   though S has all the right letters, they are not in the 
#   right order.
#
# - The word "kangaroo" is the longest word in D, but it 
#   isn't a subsequence of S.
def is_subsequence(subsequence, sequence, subsequence_length, sequence_length):
    # Base Cases
    if subsequence_length == 0:
        return True

    if sequence_length == 0:
        return False

    # Inductive Steps

    # Last characters matching
    if subsequence[subsequence_length - 1] == sequence[sequence_length - 1]:
        return is_subsequence(subsequence, sequence, subsequence_length - 1, sequence_length - 1)

    # Last characters not matching
    return is_subsequence(subsequence, sequence, subsequence_length, sequence_length - 1)

def main():
    stringtosearch = input("Please enter string: ")
    setofwords = input("Please enter dictionary: ")
    setofwords = list(setofwords.strip(','))

    # Finding longest word in dictionary that is subsequence of S
    longestword = ""
    for i in range(0, len(setofwords)):
        if is_subsequence(setofwords[i], stringtosearch, len(setofwords[i]), len(stringtosearch)):
            longestword = setofwords[i]

    print("Longest word in dictionary D: {}".format(longestword))

if __name__ == '__main__':
    main()