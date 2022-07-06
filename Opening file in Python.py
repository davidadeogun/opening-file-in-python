#Copied the file path of the csv file and loaded the dataset in my python program
#Saved the opened csv file name as "lives"
#printed each data in the csv file

from collections import Counter
import collections

with open("life-expectancy.csv") as lives:
    inter = iter(lives)  #To iterate through the dataset, I used the built in function 'iter'
    next_inter = next(inter)  #and 'next'
    
    second_data = []    #converts raw data from csv into list
      
    for line in lives:
        stripped_life = line.strip()  #Strips the raw data
        parts = stripped_life.split(",")  #splits the data into 4 parts, separated by a comma
        
        #Below is each of the sections available in the raw data, assigned to a variable
        country = parts[0]    #remains a string
        code = parts[1]     #remains a string
        year = int(parts[2]) #converts the year into an integer
        expectancy = float(parts[3])  #Converts this into a float

        second_data.append([country, code, year, expectancy])  #Moves each of the sections into a list and append to the list variable
                                                                   
value = [x[3] for x in second_data]
highest_life_expectancy = (max(value))    #highest value for life expectancy
print(f"The highest life expectancy is {highest_life_expectancy :.2f}")

value= [x[3] for x in second_data]
lowest_life_expectancy = (min(value))   #lowest value for life expectancy
print(f"The lowest life expectancy is {lowest_life_expectancy :.2f}")


over_the_years = [x[2] for x in second_data]
#print(highest_value)
#print(over_the_years)

over_the_years.sort()

#Using the sort built in function, I was able clean the data
#  by first of all sorting the life expetancy values of the dataset
value.sort()

#The I counted the number of occurences of each element in the dataset
#by using the built in 'counter'
counter = collections.Counter(value)
#print(over_the_years)
print(counter)
print()
print("The data below shows the number of occurences for each value of the life expectancy in the dataset")
print()
#Finally, I was able to see the number of times for each life expectancy value
#in the dataset. Though I plotted the graph out of python to get the visual representation
#of the dataset, but by mere looking at the output in the terminal, you can see that some values,
#occured multiple times as against those that appeared only one.
print(counter.values())  


    































