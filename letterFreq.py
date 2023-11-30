

import wordData
import matplotlib.pyplot as plt


class Letter:
    val : str
    amount : int
    
    
    def __init__(self, val, amount):
        self.val = val
        self.amount = amount
        
    def add(self, amount):
        self.amount += amount


def letterFreq(words, tup = False):
    
    
    letters = {}
    
    for word in words:
        total = wordData.totalOccurrences(word, words)
        
        for x in word:
            letters[x] = letters.get(x, 0) + total
            
    letters_l = []
    for x in letters:
        letters_l.append(Letter(x, letters[x]))
            
    letters_l = sorted(letters_l, key = lambda x: x.amount, reverse=True)
    
    letters_s = ""
    
    for x in letters_l:
        letters_s += x.val
            
    if tup:
        return letters_s, letters_l
    return letters_s
        
        
        


def main():
    
    file_name = input("Enter File Name: ")
    
    words = wordData.readWordFile(file_name)

    letters_s, letters_l = letterFreq(words, tup=True)

    print(f'Letters sorted in decreasing freqency: {letters_s}')
    
    letters_l = sorted(letters_l, key = lambda x:x.val)
    
    lets_l = []
    vals_l = []
    
    for x in letters_l:
        lets_l.append(x.val)
        vals_l.append(x.amount)
        
    
    plt.bar(lets_l, vals_l, color="skyblue")
    plt.show()
    
    
    

if __name__ == "__main__":
    main()
    