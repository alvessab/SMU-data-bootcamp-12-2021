import csv
from collections import Counter    #https://realpython.com/python-counter/

#read in pyPoll data
poll_csv= "PyPoll/PyPoll Resources/election_data.csv"
 
#declare variables
totalVotes=0
votes= []
candVotes= {}

with open(poll_csv, "r") as file:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(file, delimiter=',')

    csvheader = next(csvreader)

   # print(f"Header: {csvheader}")

    for row in csvreader:
        totalVotes +=1 #to count the total number of votes cast
        votes.append(row[2])    #list to use with counter tool

    candVotes= Counter(votes) #The total number of votes each candidate won and list of candidates
   
candDict= dict(candVotes)

#The winner of the election based on popular vote.
winner= max(candDict, key=candDict.get)     #https://pythonguides.com/python-dictionary-find-a-key-by-value/#:~:text=Python

summary = f"""Election Results
---------------
Total Votes: {totalVotes}
---------------\n"""    #add new line: https://www.askpython.com/python/examples/add-a-newline-character-in-python

for cand in candDict.keys():
    perc = 100*(candDict[cand] / totalVotes)       #The percentage of votes each candidate won
   
    summary += f"{cand}: {round(perc, 3)}% ({candDict[cand]})\n"  #https://www.w3schools.com/python/ref_func_round.asp

summary += f"""---------------
Winner: {winner}
"""

print(summary)


#test file of results
fileBank= "PyPoll/Analysis/pyPoll.txt"
file = open(fileBank, "w") 
file.write(summary)
file.close() 