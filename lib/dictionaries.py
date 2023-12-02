import string

def word_frequency(sentence):
    # Remove punctuation from the sentence
    sentence = sentence.translate(str.maketrans("", "", string.punctuation))

    # Convert the sentence to lowercase
    sentence = sentence.lower()

    # Split the sentence into words
    words = sentence.split()

    # Create a dictionary to store the frequency of each word
    frequency = {}

    # Iterate through each word in the words list
    for word in words:
        # If the word is already in the frequency dictionary, increment its count
        if word in frequency:
            frequency[word] += 1
        # Otherwise, add the word to the frequency dictionary with a count of 1
        else:
            frequency[word] = 1

    return frequency


# test case 1
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)

# test case 2
print(word_frequency("Hello, world! The world is a wonderful place."))