#PyBank

import os
import csv

csvpath = os.path.join('budget_data.csv')

Months=[]
CashFlow=[]
TotalMonths=0
CashFlowTotal=0
TotalChange=0
GreatestIncrease=0
GreatestDecrease=0
Output=[]

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader) #skips first row
    for row in csvreader:
        Months.append(row[0])
        CashFlow.append(row[1])
        TotalMonths=TotalMonths+1
        CashFlowTotal=CashFlowTotal+int(row[1])

for x in range(1,len(CashFlow)):
    change = int(CashFlow[x])-int(CashFlow[x-1])
    TotalChange=TotalChange+change
    #print(CashFlow[x])
    if change>GreatestIncrease:
        GreatestIncrease=change
        GreatestIncreaseDate=Months[x]
    if change<GreatestDecrease:
        GreatestDecrease=change
        GreatestDecreaseDate=Months[x]

AvgCashFlow=round(TotalChange/(TotalMonths-1),2)

#Assemple Output -----------------------------
Output.append("Finacial Analysis")
Output.append("-------------------------")
Output.append("Total Months: "+str(TotalMonths))
Output.append("Total: $"+str(CashFlowTotal))
Output.append("Average Change: $"+str(AvgCashFlow))
Output.append("Greatest Increase in Profits: "+GreatestIncreaseDate+" ($"+str(GreatestIncrease)+")")
Output.append("Greatest Decrease in Profits: "+GreatestDecreaseDate+" ($"+str(GreatestDecrease)+")")

#Write to CSV ----------------------------

# Specify the file to write to
output_path = os.path.join("PyBank_Output.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=' ',escapechar=' ',quoting=csv.QUOTE_NONE)

    # Write the rows
    for x in Output:
        csvwriter.writerow([x])
        print(x)