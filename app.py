

""" values = [1,2.23,5,7,2,30,15]
print(values[0])
print(values[6]) """

""" day_of_week = input("Are you failing this class ")
if day_of_week == "yes bro":
    print("correct")
else:
    print("incorrect") """

# Pseudocode:
# Ask the user to enter a sentence.
# Define a function that accepts the sentence.
# Split the sentence into a list of words.
# Count the words in the list.
# Return the word count.
# Display the word count to the user.


def y(sentence):
    words = sentence.split()
    return len(words)


sentence = input("Enter a sentence: ")
print(f"That sentence has {y(sentence)} words.")
