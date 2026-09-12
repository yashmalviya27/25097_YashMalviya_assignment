# Exercise 1: Sentence Analysis (Character & Word Count)


def sentence_analysis():
    sentence = input("Enter a sentence: ")
    num_characters = len(sentence)
    num_words = sentence.split(" ")
    num_words = len(num_words)
    print(f"Total Characters: {num_characters}")
    print(f"Total Words: {num_words}")


sentence_analysis()
