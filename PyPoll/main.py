#import CSV file
#import os module
import os
import csv

#define path to resources file
pypoll = os.path.join("resources","election_data.csv")

with open(pypoll) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    #CSV Header: ['Voter ID', 'County', 'Candidate']...[0.1.2]

    #Total Votes = length of list - headers
    list_length = [row for row in csvreader]
    total_votes = (len(list_length))
    #print("Total Votes: ", total_votes)

#List for Candidate Vote Tally
candidates = {}
for row in list_length:
    if row[2] not in candidates.keys():
        candidates[row[2]] = 1
    else:
        candidates[row[2]]+= 1

#print(candidates)

#Candidate vote count
khan_c = candidates['Khan']
correy_c = candidates['Correy']
li_c = candidates['Li']
o_tooley_c = candidates["O'Tooley"]


#Candidate % of vote
khan_p = round(((candidates['Khan']/total_votes)*100),3)
correy_p = round(((candidates['Correy']/total_votes)*100),3)
li_p = round(((candidates['Li']/total_votes)*100),3)
o_tooley_p = round(((candidates["O'Tooley"]/total_votes)*100),3)

print("Election Results")
print("--------------------------")
print("Total Votes: ", total_votes)
print("--------------------------")
print("Khan: ",khan_p,"%","(",khan_c,")")
print("Correy: ",correy_p ,"%","(",correy_c,")")
print("Li: ",li_p ,"%","(",li_c,")")
print("O'Tooley: ",o_tooley_p ,"%","(",o_tooley_c,")")
print("--------------------------")
print("Winner: ", "Khan")