import os
import csv

totalVotes = 0
candidateList = []
voteCountList = []
dataFileList = ["election_data.csv"]

for file in dataFileList:
    csvpath = os.path.join("Resources",file)
    print(csvpath)
    with open(csvpath, newline='') as csvfile:
        csvfile.readline()
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            totalVotes = totalVotes+1
            candidate = row[2]
            if not candidate in candidateList:
               candidateList.append(candidate)
               voteCountList.append(1)
            else:
                indexofCandidate =  candidateList.index(candidate)
                curVoteTally = voteCountList[indexofCandidate]
                voteCountList[indexofCandidate] = curVoteTally+1
                        
outputpath = os.path.join("Resources","Pypoll_Results.txt")

resultsfile = open(outputpath, "w")

lines = []
lines.append("Election Results")
lines.append("-------------------------")
lines.append("Total Votes: "+str(totalVotes))
lines.append("-------------------------")
winningVotes = 0
for candidate in candidateList:
    votes = voteCountList[candidateList.index(candidate)]
    pctVotes = (votes/totalVotes)*100
    if votes > winningVotes:
        winner = candidate
        winningVotes = votes
    lines.append(candidate+": "+str(round(pctVotes,2))+"% "+"("+str(votes) +")")
lines.append("-------------------------")
lines.append("Winner: "+winner)
for line in lines:
    print(line)
    print(line,file=resultsfile)
resultsfile.close()  