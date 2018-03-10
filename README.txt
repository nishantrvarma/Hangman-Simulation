# Type 1:

This program makes use of regular expressions and conditional probability. Though the program works as intended, it's results are skewed primarily due to its inability to comprehend context. While the program succesfully guesses most of the letters, it fails to guess the last 2-3 letters in most situations. This problem may be circumvented to an extent by having a "common-words" dictionary as this will allow the program to give more weight to the commonly used words.


# Type 2:

This program improves on the former in terms of success ratio. It prompts the user to guess the final 2 characters if there is only 1 chance left. This approach was decided upon as on examination of the previous program, it was observed that most of the users failed due to one or two characters not being able to be guessed by the program as it lacks the ability to understand context. However as humans are more than capable in this aspect, a mix of both sides provides the highest success ratio while trading off on the automation. 
