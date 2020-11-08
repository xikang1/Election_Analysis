# the data needed to be retrieved
#1:  the total number of votes cast
#2: candidates name
#3:the percentage of votes each candidate won
#4:the total number of votes each canadidate won
#5: the winner
import csv
import os


#assigning a variable to the dataset
#file_to_load = "election_results.csv"
#election_data = open(file_to_load,'r') # read the data from file to load

file_to_load = os.path.join("election_results.csv") # importing data by using os function
file_to_save = os.path.join("election_analysis.txt") # assign a variable to save the file to a path

with open(file_to_load) as election_data: # using with statement to access data

    file_reader = csv.reader(election_data) #read the file object by reader function
    #for row in file_reader: # print each row in the reader
    #    print(row)
    headers=next(election_data)
    print(headers)
    

