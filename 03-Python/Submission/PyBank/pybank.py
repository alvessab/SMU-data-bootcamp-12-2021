import csv

#read in Pybank data
bank_csv= "PyBank/PyBank Resources/budget_data.csv"

#declare variables
months=0
total=0
changes=[]
changesMonths=[]
previousProfit= 0 #start loop where relevant correctly
changesDict= {}

with open(bank_csv, "r") as file:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(file, delimiter=',')

    csvheader = next(csvreader)

    #print(f"Header: {csvheader}")

    for row in csvreader:
        months += 1 #counter for total number of months
        sen_months= f"Months in data set: {months}"

        total += int(row[1]) #calculate net total amount of profit/losses over the entire period
        sen_total= f"The net total amount of Profit/Losses over the entire period is: ${total}"
    

        # Calculate the changes in "Profit/Losses" over the entire period  
        change= int(row[1]) - previousProfit
        changes.append(change) #add values to changes list
        changesMonths.append(row[0]) #add months to changesMonths list
        previousProfit= int(row[1]) #follow through for next loop
        changesDict = {changesMonths[row]: changes[row] for row in range(len(changesMonths))} #https://www.tutorialspoint.com/convert-two-lists-into-a-dictionary-in-python

        
#Find average of changes of Profits/Losses over the Period
avgChange= sum(changes) / months
sen_avgChange= f"The average of changes of Profits/Losses over the Period is: {avgChange}"

#The greatest increase in profits (date and amount) over the entire period
maxChange= max(changes) #get max from list of changes
maxChangeMonth=max(changesDict, key=changesDict.get) #get month(key) of max from dictionary
maxChangeResult= f"[{maxChangeMonth}, ${maxChange}]"
sen_maxChangeResult= f"The greatest increase in profits (date and amount) over the entire period is: {maxChangeResult}"

# The greatest decrease in profits (date and amount) over the entire period
minChange= min(changes) #get min from list of changes
minChangeMonth=min(changesDict, key=changesDict.get) #find key in dictionary
minChangeResult= f"[{minChangeMonth}, ${minChange}]"
sen_minChangeResult= f"The greatest decrease in profits (date and amount) over the entire period is: {minChangeResult}"

summary= f"""FINANCIAL ANALYSIS: 
{sen_months}
{sen_total}
{sen_avgChange}
{sen_maxChangeResult}
{sen_minChangeResult}"""

print(summary)

#test file of results resource: https://www.codegrepper.com/code-examples/python/python+create+text+file+in+specific+directory
fileBank= "PyBank/Analysis/pyBank.txt"
file = open(fileBank, "w") 
file.write(summary)
file.close() 