import wordData
import printedWords
import letterFreq
import matplotlib.pyplot as plt



def trending(words, startYr, endYr):
    
    
    trending = []
    
    for x in words:
        start_val = words[x].get(startYr, 0)
        end_val = words[x].get(endYr, 0)
        
        if start_val >=1000 and end_val>= 1000:
            trending.append((x, end_val/start_val))
            
    trending = sorted(trending, key= lambda x: x[1], reverse=True)
    return trending


def main():
    
    
    file_name = input("Enter word file name: ")
    start_yr = int(input("Enter start year: "))
    end_yr = int(input("Enter end year: "))

    
    data_dict = wordData.readWordFile(file_name=file_name)

    trend_l = trending(data_dict, start_yr, end_yr)

    if len(trend_l) < 20:
        middle = len(trend_l) // 2
        
        front = trend_l[0:middle]
        back = trend_l[middle:]
        
    else:
        front = trend_l[0:10]
        back = trend_l[-10:]

    
    print(f'The top {len(front)} trending words from {start_yr} to {end_yr}: ')
    for x in front:
        print(x[0])

    print("\n")

    print(f'The bottom {len(back)} trending words from {start_yr} to {end_yr}: ')
    for x in back[-1::-1]:
        print(x[0])
        
        

if __name__ == "__main__":
    main()