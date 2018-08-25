#PyPoll

import os
import csv

csvpath = os.path.join('election_data.csv')

Candidate=[]
Votecount=[]
County=[]
CountyCount=[]
VotePercent=[]
Output=[]
TotalVotes=0

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader) #skips first row
    for row in csvreader:
       
       TotalVotes=TotalVotes+1
        
       if row[2] in Candidate:
            Votecount[Candidate.index(row[2])]=Votecount[Candidate.index(row[2])]+1
            VotePercent[Candidate.index(row[2])]=format((Votecount[Candidate.index(row[2])]/TotalVotes)*100,'.3f')
            if max(Votecount)==Votecount[Candidate.index(row[2])]:
                Winner=row[2]
       else:
            Candidate.append(row[2])
            Votecount.append(1)
            VotePercent.append(0)

Output.append('Election Results')
Output.append('-------------------')
Output.append('Total Votes: '+str(TotalVotes))
Output.append('-------------------')
for x in range(len(Candidate)):
    Output.append(Candidate[x]+": "+str(VotePercent[x])+"% ("+str(Votecount[x])+")")
Output.append('-------------------')
Output.append('Winner: '+str(Winner))
Output.append('-------------------')

# Specify the file to write to
output_path = os.path.join("PyPoll_Output.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=' ',escapechar=' ',quoting=csv.QUOTE_NONE)

    # Write the rows
    for x in Output:
        csvwriter.writerow([x])
        print(x)
