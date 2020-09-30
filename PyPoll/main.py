import os
import csv

# Collect data from csv file in the resources folder
PyPoll_path = os.path.join('Resources', 'election_data.csv')

# Define lists to add value from csv file
total_votes=[]
voter_ID=[]
county=[]
candidate=[]
khan=[]
correy=[]
li=[]
otooley=[]

# Read the csv file

with open(PyPoll_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    # Skip the header to start counting the first record
    csv_header = next(csvreader)

    # count the total votes

    for row in csvreader:
        voter_ID.append(int(row[0]))
        county.append(row[1])
        candidate.append(row[2])

# Count total votes

total_votes = len(voter_ID)

# Count votes for each candidate

for candidate in candidate:
    if candidate == "Khan":
        khan.append(candidate)
        khan_total_votes = len(khan)
    elif candidate == "Correy":
        correy.append(candidate)
        correy_total_votes = len(correy)
    elif candidate == "Li":
        li.append(candidate)
        li_total_votes = len(li)
    else:
        otooley.append(candidate)
        otooley_total_votes = len(otooley)

# Calculate percentage of votes for each candidate
percentage_for_khan = khan_total_votes/total_votes
percentage_for_correy = correy_total_votes/total_votes
percentage_for_li = li_total_votes/total_votes
percentage_for_otooley = otooley_total_votes/total_votes

# Adding conditions for identifying winner of election
if percentage_for_khan > max(percentage_for_correy, percentage_for_li, percentage_for_otooley):
    winner_of_election = "Khan"
elif percentage_for_correy > max(percentage_for_khan, percentage_for_li, percentage_for_otooley):
    winner_of_election = "Correy"
elif percentage_for_li > max(percentage_for_khan, percentage_for_correy, percentage_for_otooley):
    winner_of_election = "Li"
else:
    winner_of_election = "O'Tooley"
    

# Print final result for Election Results:
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
#print("Khan: " + str(candidate_khan))
print(f"Khan: {percentage_for_khan:.3%} ({khan_total_votes})")
print(f"Correy: {percentage_for_correy:.3%} ({correy_total_votes})")
print(f"Li: {percentage_for_li:.3%} ({li_total_votes})")
print(f"O'Tooley: {percentage_for_otooley:.3%} ({otooley_total_votes})")
print("-------------------------")
print("Winner: " + str(winner_of_election))
print("-------------------------")

# Export a text file for the final result
Election_Results = os.path.join("Election_Results.txt")
with open(Election_Results, "w") as datafile:

    datafile.write("Election Results" + "\n")
    datafile.write("-------------------------" + "\n")
    datafile.write("Total Votes: " + str(total_votes) + "\n")
    datafile.write("-------------------------" + "\n")
    datafile.write(f"Khan: {percentage_for_khan:.3%} ({khan_total_votes}) \n")
    datafile.write(f"Correy: {percentage_for_correy:.3%} ({correy_total_votes}) \n")
    datafile.write(f"Li: {percentage_for_li:.3%} ({li_total_votes}) \n")
    datafile.write(f"O'Tooley: {percentage_for_otooley:.3%} ({otooley_total_votes}) \n")
    datafile.write("-------------------------" + "\n")
    datafile.write("Winner: " + str(winner_of_election) + "\n")
    datafile.write("-------------------------") 
   
