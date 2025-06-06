# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        '''Returns a list of words from word_list that are anagrams of the initialized word.'''
        # Sort the letters in the word and compare to sorted letters of each word in the list
        return [word for word in word_list if sorted(word) == sorted(self.word)]
