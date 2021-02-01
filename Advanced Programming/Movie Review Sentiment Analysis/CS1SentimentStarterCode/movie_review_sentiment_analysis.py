'''Movie Review Sentiment Analysis

    William Ikenna-Nwosu

    Sentiment Analysis is a Big Data problem which seeks to determine the general attitude
    of a writer given some text they have written. For 
    instance, we would like to have a program that could look 
    at the text “The film was a breath of fresh air” and 
    realize that it was a positive statement while “It made me 
    want to poke out my eye balls” is negative.

    One algorithm that we can use for this is to assign 
    a numeric value to any given word based on how 
    positive or negative that word is and then score the 
    statement based on the values of the words. But, how 
    do we come up with our word scores in the first place?
    
    That’s the problem that we’ll solve in this assignment. You are going to search through a
    file containing movie reviews from the Rotten Tomatoes 
    website which have both a numeric score as well as text.

    Note that each review starts with a number 0 through 
    4 with the following meaning:
    • 0 : negative
    • 1 : somewhat negative
    • 2 : neutral
    • 3 : somewhat positive
    • 4 : positive

    1. (30 points) For the base assignment, you will ask 
    the user to enter a word, and then you will search 
    every movie review for that word. If you find it, add 
    the score for that review to the word’s running score 
    total (i.e., an accumulator variable). You also will 
    need to keep track of how many appearances the word 
    made so that you can report the average score of 
    reviews containing that word back to the user.

    2. (10 points) For an additional 10 points, ask the user 
    to give you the name of a file containing a series of 
    words, one-per-line, and compute the score of every word 
    in the file. Report back to the user the average score 
    of the words in the file. This will allow you to predict 
    the overall sentiment of the phrase represented by words 
    in the file. Consider an average word score above 2.01 
    as an overall positive sentiment and consider average
    score below 1.99 to have an overall negative sentiment. 
    As an example, for a file called negTest.txt containing 
    words...

    3. (10 points) For an additional 10 points, ask the user 
    to give you the name of a file containing a series of 
    words, one-per-line, and compute the score of every 
    word in the file. Report back to the user which word 
    was the most positive and which was the most negative.
'''
def calculate_average_score(word, data):
    '''Function to calculate the average score of a word

    Args:
        word(str): word
        data(list): data

    Raises:

    Return wordscore / number_of_reviews_appears_in

    '''
    wordscore = 0
    number_of_occurences_of_word = 0
    number_of_reviews_appears_in = 0
    flag = False
    for i in range(0, len(data)):
        for j in range(1, len(data[i])):
            if word.lower() == data[i][j].lower():
                flag = True
                number_of_occurences_of_word += 1
        if flag:
            wordscore += data[i][0]
            number_of_reviews_appears_in += 1
        flag = False
    
    if wordscore == 0 or number_of_reviews_appears_in == 0:
        return 0

    return wordscore / number_of_reviews_appears_in

def calculate_sentiment(wordscore):
    '''Function to calculate sentiment of a word in a review

        Args:
            wordscore(int): wordscore

        Raises:

        Return sentiment
    '''
    rounded_wordscore = int(round(wordscore))
    if rounded_wordscore <= 1:
        return 'negative' 
    elif rounded_wordscore >= 3:
        return 'positive'
    else:
        return 'neutral'
     
def main():
    # 1. Base assignment
    # File Processing
    path = 'movieReviews.txt'
    data = [] # List to hold lines in file
    with open(path, 'r') as f:
        for line in f:
            data.append(line.split(" "))

    # Convert scores from str to int
    for i in range(0, len(data)):
        data[i][0] = int(data[i][0])
    
    # Ask user for input
    word = input("Enter a word: ")

    # Count how many times this word appears in the DB and keep track of scores of reviews it appears in
    wordscore = 0
    number_of_occurences_of_word = 0
    number_of_reviews_appears_in = 0
    flag = False
    for i in range(0, len(data)):
        for j in range(1, len(data[i])):
            if word.lower() == data[i][j].lower():
                flag = True
                number_of_occurences_of_word += 1
        if flag:
            wordscore += data[i][0]
            number_of_reviews_appears_in += 1
        flag = False
    
    # Show results to user
    print('{} appears {} times.'.format(word, number_of_occurences_of_word))
    print('{} appears in {} reviews.'.format(word, number_of_reviews_appears_in))
    print('The average score for reviews containing the word {} is {}'.format(word, wordscore / number_of_reviews_appears_in))
    f.close() # Close the file

    # 2. Extra 10 points
    userinputfilename = input("Enter the name of the file with words you want to find the average score for: ")
    words = []
    with open(userinputfilename, 'r') as f:
        for line in f:
            words.append(line.rstrip())
    
    # Calculate overall average score of words in file
    average_scores = []
    words_and_average_scores_dict = {}
    for word in words:
        average_scores.append(calculate_average_score(word, data))
        words_and_average_scores_dict[word] = calculate_average_score(word, data)
    overall_average_score = sum(average_scores) / len(average_scores)

    # Calculate overall sentiment of file
    sentiment = calculate_sentiment(overall_average_score)

    # Show results
    print('The average score of words in {} is {}'.format(userinputfilename, overall_average_score))
    print('The overall sentiment of {} is {}'.format(userinputfilename, sentiment))

    # 3. Additional 10 points
    new_list = sorted(words_and_average_scores_dict.items(), key = lambda kv: (kv[1]))
    print('The most negative word, with a score of {} is {}'.format(new_list[0][1], new_list[0][0]))
    print('The most positive word, with a score of {} is {}'.format(new_list[len(new_list) - 1][1], new_list[len(new_list) - 1][0]))

    # 4. Additional 10 points
    path1 = 'negative.txt'
    path2 = 'positive.txt'
    outputfile1 = open(path1, "w")
    outputfile2 = open(path2, "w")
    for i in range(0, len(new_list)):
        if new_list[i][1] <= 1.9:
            outputfile1.write(new_list[i][0] + '\n')
        elif new_list[i][1] >= 2.1:
            outputfile2.write(new_list[i][0] + '\n')

    
if __name__ == '__main__':
    main()