import numpy as np
import wordData
import printedWords



def get_year_distrib(words):
    
    
    nl = []
    for x in words:
        for year in words[x]:
            nl.append(year)
            
    start = min(nl)
    end = max(nl)
    

    return list(range(start, end+1))


def normal_dot(word_dict, word):
    
    years = get_year_distrib(word_dict)

    values_word = []
    
    
    for x in years:
        values_word.append(word_dict[word].get(x, 0))

    values_word = np.array(values_word)

    words_value = []
    words_l = []
    values_word = np.array(values_word) / np.linalg.norm(values_word)
    
    
    for x in word_dict:
        words_l.append(x)
        words_value1 = []
        for j in years:
            words_value1.append(word_dict[x].get(j, 0))
            
        
        if x == word:
            tmp = np.array(words_value1) / np.linalg.norm(words_value1)
            
        
        tmp = np.array(words_value1) / np.linalg.norm(words_value1)
        words_value.append(tmp)
            

    words_value = np.array(words_value)


    vectorized_vals = words_value.dot(values_word)
    

    return vectorized_vals, words_l


    
    

def topSimilar(words, word):
    
    
    words_vals, words_l = normal_dot(words, word)
    val_to_word = dict(zip(words_vals, words_l))
    
    
    
    

    top_five = []
    words_vals = words_vals.tolist()
    
    for x in range(min(len(words_vals), 5)):
        top_five.append(max(words_vals))
        words_vals.remove(top_five[-1])
    
        
    top_five_words = [val_to_word[x] for x in top_five]

    
    return top_five_words



def main():
    file_name = input("Enter word file name: ")
    word = input("Enter word: ")
    words = wordData.readWordFile(file_name=file_name)
    top_five = topSimilar(words, word)
    print("\n")
    print("The most similar words are: ")
    for x in top_five:
        print(x)
        


if __name__ == "__main__":
    main()