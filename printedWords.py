


import wordData
import matplotlib.pyplot as plt


def printedWords(words):
    
    """takes in words dictionary and 

    Returns:
        _type_: _description_
    """

    
    data_dict = {}
    
    for x in words:
        for year in words[x]:
            data_dict[year] = data_dict.get(year, 0) + words[x][year]
            
            
    data_arr = []
    
    
    for x in data_dict:
        data_arr.append([x, data_dict[x]])
    
    
    new_arr = sorted(data_arr, key = lambda x: x[0])
    
    new_arr = [(x[0], x[1]) for x in new_arr]
    
    return new_arr

    
def wordsForYear(year, yearList, offset=0, return_ind=False):
    
    if len(yearList) == 1 and yearList[0][0] != year:
        return 0
    
    middle = len(yearList) // 2 
    
    if yearList[middle][0] == year:
        if return_ind:
            return yearList[middle][1], middle+offset
        return yearList[middle][1]
            
    
    if yearList[middle][0] > year:
        return wordsForYear(year, yearList[0:middle], offset, return_ind)
    return wordsForYear(year, yearList[middle:], offset+middle, return_ind)
    
    
def plot_graph(year_arr):
    
    years = [x[0] for x in year_arr]
    values = [x[1] for x in year_arr]
    
    plt.plot(years, values)
    plt.show()

    return 

    
def main():
    
    
    file_name = input("Enter Data File Name: ")
    year = int(input("Enter Year: "))

    data_dict = wordData.readWordFile(file_name=file_name)
    year_arr = printedWords(data_dict)
    ans, ind = wordsForYear(year=year, yearList=year_arr, return_ind=True)
    print(f'Total printed words in {year}: {ans}, {year_arr[ind]}')
    plot_graph(year_arr)
    

if __name__ == "__main__":
    main()




