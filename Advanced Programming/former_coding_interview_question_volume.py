# William Ikenna-Nwosu (wiknwo)
# 
# Imagine an island that is in the shape of a bar graph. 
# When it rains, certain areas of the island fill up with 
# rainwater to form lakes. Any excess rainwater the island 
# cannot hold in lakes will run off the island to the west or 
# east and drain into the ocean.
#
# Given an array of positive integers representing 2-D bar 
# heights, design an algorithm (or write a function) that can 
# compute the total volume (capacity) of water that could be 
# held in all lakes on such an island given an array of the 
# heights of the bars. Assume an elevation map where the width 
# of each bar is 1.
#
# Example: Given [1,3,2,4,1,3,1,4,5,2,2,1,4,2,2], return 
# 15 (3 bodies of water with volumes of 1,7,7 yields total 
# volume of 15)
def main():
    bar_heights = input('Enter bar heights separated by space: ').split(" ")
    bar_heights = list(map(int, bar_heights))
    print(bar_heights)
    volume = []

    # Fill volume list with zeroes
    for i in range(0, len(bar_heights)):
        volume.append(0)

    # Calculate volume of bar heights that can be filled
    for i in range(1, len(bar_heights) - 1):
        # Find a gap
        if bar_heights[i - 1] > bar_heights[i] and bar_heights[i + 1] > bar_heights[i]:
            while (bar_heights[i] + volume[i]) < min(bar_heights[i - 1], bar_heights[i + 1]):
                volume[i] = volume[i] + 1
    print(volume)
if __name__ == '__main__':
    main()