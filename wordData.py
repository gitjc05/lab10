


def readWordFile(file_name):
    """ reads a text file and turns it into a dictionary with using words as keys to values of year and count

    Args:
        file_name (string): file name

    Returns:
        dict: dictionary of words as keys to years as keys to values
    """

    file_location = "data/"+file_name
    
    
    with open(file_location) as f:
        word_list = f.readlines()
        
        
        data_dict = {}
        
        cur = ""
        
        for x in word_list:
            
            if not x[0].isdigit():
                cur = x.strip()
                data_dict[cur] = {}
            else:
                new_s = x.strip()
                new_l = new_s.split(",")
                data_dict[cur][int(new_l[0])] = int(new_l[1])
                
        return data_dict
    

def totalOccurrences(word, words):
    """counts the occurences of a given word in a given dictionary

    Args:
        word (string): word to search for
        words (dictionary): dictionary of words and values of occurences

    Returns:
        int: total occurences of word
    """
    
    if not words.get(word, False):
        return 0
    ans = 0
    for x in words[word]:
        ans += words[word][x]
    
    
    return ans
    

def main():
    """main function
    takes in file name and word
    shows the total occurences of the word
    """
    file_name = input("Enter file name: ")
    word = input("Enter Word: ")
    print("Total Occurrences of "+word+": ",totalOccurrences(word, readWordFile(file_name)))


if __name__ == "__main__":
    main()
    