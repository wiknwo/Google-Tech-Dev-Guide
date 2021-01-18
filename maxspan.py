# William Ikenna-Nwosu (wiknwo)
# 
# Consider the leftmost and righmost appearances of some 
# value in an array. We'll say that the "span" is the number 
# of elements between the two inclusive. A single value has a 
# span of 1. Returns the largest span found in the given array. (Efficiency is not a priority.)
#
# maxSpan([1, 2, 1, 1, 3]) → 4
# maxSpan([1, 4, 2, 1, 4, 1, 4]) → 6
# maxSpan([1, 4, 2, 1, 4, 4, 4]) → 6
def maxspan(numbers):
    maximumspan = 0
    if len(numbers) == 1:
        return 1
    
    for i in range(0, len(numbers) - 1):
        count = len(numbers) - 1

        # Counting number of elements between the two inclusive
        while(numbers[i] != numbers[count]):
            count = count - 1
        
        # Calculating span
        span = count - i + 1
        if span > maximumspan:
            maximumspan = span
    return maximumspan

def main():
    print(maxspan([1, 2, 1, 1, 3]))

if __name__ == '__main__':
    main()