# PyPoll
import csv
import os

# insure that the Terminal's working directory is
#   ~/../Homework/python-challenge/PyPoll

# set up file interfaces
inputfile = 'election_data.csv'
#inputfile = 'test_file.csv'       # truncated version for testing
outputfile = 'election_analysis.csv'
input_path = os.path.join('.', 'Resources', inputfile)
output_path = os.path.join('.', 'Output', outputfile)

# read the voting data
with open(input_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)   # discard header
    candidate_tally = {}           # a dictionary for the voting data for each candidate 
    vote_total = 0                 # the total number of votes cast

    # evaluate first vote (first row)
    first_row = next(csvreader)
    winner = first_row[2]          # the winner, which starts with the first vote
    candidate_tally[first_row[2]] = 1
    vote_total += 1

    # evaluate remaining rows
    for row in csvreader:
        voter_id = row[0]
        if voter_id != "":         # skip invalid row (no voter ID)
            county = row[1]        # the county in which the vote was cast
            candidate = row[2]     # the candidate for whom was voted 
            vote_total += 1
            if candidate in candidate_tally:
                # increment the tally for the candidate
                candidate_tally[candidate] += 1
            else:
                # add the candidate to the tally dictionary
                candidate_tally[candidate] = 1

# find the winner
for candidate in candidate_tally:
    if  candidate_tally[candidate] > candidate_tally[winner]:
        winner = candidate

print("")
print("Election Results")
print("---------------------------------")
print(f"Total Votes:  {vote_total}")
print("---------------------------------")
for candidate in candidate_tally:
    tally = candidate_tally[candidate]
    percentage = (tally/vote_total) * 100
    # percentage is displayed with two decimal points
    print(f"{candidate}: {percentage:.2f}%  ({tally})")
print("---------------------------------")
print(f"Winner is {winner}")
print("---------------------------------")
print("")

# repeat print, but into a csv file
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["---------------------------------"])
    csvwriter.writerow([f"Total Votes:  {vote_total}"])
    csvwriter.writerow(["---------------------------------"])
    for candidate in candidate_tally:
        tally = candidate_tally[candidate]
        percentage = (tally/vote_total) * 100
        # percentage is displayed with two decimal points
        csvwriter.writerow([f"{candidate}: {percentage:.2f}%  ({tally})"])
    csvwriter.writerow(["---------------------------------"])
    csvwriter.writerow([f"Winner is {winner}"])
    csvwriter.writerow(["---------------------------------"])
