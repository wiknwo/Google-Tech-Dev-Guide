# William Ikenna-Nwosu (wiknwo)
# 
# Alice has n candies, where the ith candy is of type 
# candyType[i]. Alice noticed that she started to gain 
# weight, so she visited a doctor.
# 
# The doctor advised Alice to only eat n / 2 of the 
# candies she has (n is always even). Alice likes her 
# candies very much, and she wants to eat the maximum 
# number of different types of candies while still 
# following the doctor's advice.
# 
# Given the integer array candyType of length n, return 
# the maximum number of different types of candies she 
# can eat if she only eats n / 2 of them.
def distributeCandies(candyType):
    difftypescandy = set() # Set holding different types of candy
    doctor_recommendation = len(candyType) / 2
    for i in range(0, len(candyType)):
        if (candyType[i] not in difftypescandy) and (len(difftypescandy) < doctor_recommendation):
            difftypescandy.add(candyType[i])
    return len(difftypescandy)

def main():
    print(distributeCandies([1, 1, 2, 3]))
if __name__ == '__main__':
    main()