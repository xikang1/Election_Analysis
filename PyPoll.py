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

total_votes = 0
candidate_options = []
candidate_votes = {}# create the dictionary forcountting votes
winning_candidate = "" # set it to str
winning_count = 0
winning_percentage = 0
with open(file_to_load) as election_data: # using with statement to access data

    file_reader = csv.reader(election_data) #read the file object by reader function

    headers=next(election_data)# read the header row
    for row in file_reader: # print each row in the reader
       total_votes +=1 # count up all the votes
       candidate_name = row[2] # get the candidate name from each row
       if candidate_name not in candidate_options: # check if the name is added to the list already
           candidate_options.append(candidate_name) # adding names to the list

           candidate_votes[candidate_name] = 0 # setting each candidate's vote =0
       candidate_votes[candidate_name] +=1
    for candidate_name in candidate_votes:
      votes = candidate_votes[candidate_name]
      vote_percentage = float(votes)/float(total_votes)*100
      print(f"{candidate_name}:{vote_percentage:.1f}%({votes:,})") 
         #determin winning count
      if (votes > winning_count) and (vote_percentage >  winning_percentage):
          winning_count = votes
          winning_percentage = vote_percentage
          winning_candidate = candidate_name
    winning_candidate_summary=(
       f"--------------------------\n"
       f"Winner:{winning_candidate}\n"
       f"Wining Vote Count:{winning_count}\n"
       f"Winning Percentage:{winning_percentage:.1f}%\n"
    )   

print(winning_candidate_summary)

    

