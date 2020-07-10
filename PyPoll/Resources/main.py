import os
import csv

csvpath = os.path.join("..", "Resources", "election_data.csv")
total = 0
total_votes = 0
candidate_list = ["khan", "correy", "li", "o'tooley"]
votes_list = [0, 0 , 0, 0]  # ["330", "200", "50", "3"]
vote_percentage = []
previous = 0
sum = 0



# Open and read csv
with open (csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    #print (csvreader)
    
   

# Read the header row first
#  ["VoterID", "County", "Candidate"]
    csv_header = next(csvreader)
   
    #print(f"CSV Header: {csv_header}")
    for row in csvreader:
        if (row[2] == "Khan"):
            votes_list[0] = votes_list[0] + 1
        if (row[2] == "Correy"):
            votes_list[1] = votes_list[1] + 1
        if (row[2] == "Li"):
            votes_list[2] = votes_list[2] + 1
        if (row[2] == "O'Tooley"):
            votes_list[3] = votes_list[3] + 1
          
        # print(row[1])
        total = total + 1



print(votes_list)
print(total)

# The total number of votes cast
# [2218231, 704200, 492940, 105630]
# Name list
# Percentage


#  Persons Name   votes  (percent)

vote_percentage = [ round(i/total*100,3)  for i in votes_list]

print(vote_percentage)


# A complete list of candidates who received votes
print('-------------------------------')

for i in range(4):
    print(f'{candidate_list[i]}  {vote_percentage[i]}  ({votes_list[i]})')

# The total number of votes each candidate won


# The winner of the election based on the popular vote

print("-------------------------------")
print(f"{total}")
print(f"candidate:  {candidate_list}")
print(f"percentage:  {vote_percentage}")
print(f'{candidate_list[0]}   ({votes_list[0]})')
print(f'{candidate_list[1]}   ({votes_list[1]})')
print(f'{candidate_list[2]}   ({votes_list[2]})')
print(f'{candidate_list[3]}   ({votes_list[3]})')
print("Winner: Khan")

txtpath = os.path.join("election_data.txt")
with open(txtpath, "w") as txtfile:
    msg1 = f"{total}\n"
    msg2 = f"candidate:  {candidate_list}\n"
    msg3 = f"percentage:  {vote_percentage}\n"
    msg4 = f"{candidate_list[0]}   ({votes_list[0]})\n"
    msg5 = f"{candidate_list[1]}   ({votes_list[1]})\n"
    msg6 = f'{candidate_list[2]}   ({votes_list[2]})\n'
    msg7 = f'{candidate_list[3]}   ({votes_list[3]})\n'
    msg8 = "Winner: Khan\n"

    txtfile.write(msg1)
    txtfile.write(msg2)
    txtfile.write(msg3)
    txtfile.write(msg4)
    txtfile.write(msg5)
    txtfile.write(msg6)
    txtfile.write(msg7)
    txtfile.write(msg8)
    

    