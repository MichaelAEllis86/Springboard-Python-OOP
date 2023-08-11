"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:

    def __init__(self,path):
        """initializes instance by taking in the path of a text file of words in string format for example words=WordFinder('words.text')
        then func makes a list out of words in file using the function parse and makes the attribute history as an empty list
        
        """
        file=open(path)
        self.words=self.parse(file)
        self.history=[]
        print(f"{len(self.words)} words read")

    def parse(self,file):
        """Parses text file into a usable list of words."""
        return[word.strip() for word in file]
    
    def random_word(self):
        """returns a random word from list of words returned by parse func. Adds random word to the history"""
        rword=random.choice(self.words)
        self.history.append(rword)
        return rword
         
    def words_produced(self):
        """returns the history list for user reference"""
        return self.history
    
    def reset_word_history(self):
        """resets the history list"""
        self.history=[]
        return "history reset!"

class SpecialWordFinder(WordFinder):
     
    #  def __init__(self,path):
    #     file=open(path)
    #     self.words=self.parse(file)
    #     self.history=[]
    #     print(f"{len(self.words)} words read")
     def __init__(self, path):
         super().__init__(path)
    
     def parse(self,file):
        """Parses text file into a usable list of words. zippy!"""
        return[word.strip() for word in file if word.strip() and not word.startswith("#")]
    
