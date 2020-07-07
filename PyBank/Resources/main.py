import os
import csv

csvpath = os.path.join("..", "Resources", "budget_data.csv")
total = 0
total_profit_loss = 0
net_change = 0
previous = 0
sum = 0
greatest_change = 0
greatest_month = ""
smallest_change = 999999
smallest_month = ""

# Open and read csv
with open (csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    print (csvreader)
    
   

# Read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    for row in csvreader:
       # print(row[1])
        total = total + 1
        total_profit_loss = total_profit_loss + int(row[1])

        net_change = int(row[1]) - previous
        if net_change > greatest_change: 
            greatest_change = net_change
            greatest_month = row[0]
        if net_change < smallest_change: 
            smallest_change = net_change
            smallest_month = row[0]


        if total > 1: 
            sum = sum + net_change
        previous = int(row[1])


average = sum/(total - 1)
        
print("financial analysis")
print("--------------------------------")
print(f"total months: {total}")
print(f"total: {total_profit_loss}")
print(f"average change: {average}")
print(f"greatest change: {greatest_month} {greatest_change}")
print(f"smallest change: {smallest_month} {smallest_change}")

# Total number of months included in dataset
    #print(count)

# Total amount of "Profit/Losses" over the entire period
    #print(total)

# The average of the changes in the "Profit/Losses" over the entie period

# The greatest increase in losses (date and amount) over the entire period


# The greatest decrease in losses (date and amount) over the entire period

txtpath = os.path.join("budget_analysis.txt")
with open(txtpath, "w") as txtfile:
    msg1 = "financial analysis\n"
    msg2 = f"total months: {total}\n"
    msg3 = f"total: {total_profit_loss}\n"
    msg4 = f"average change: {average}\n"
    msg5 = f"greatest change: {greatest_month} {greatest_change}\n"
    msg6 = f"smallest change: {smallest_month} {smallest_change}\n"
    
    txtfile.write(msg1)
    txtfile.write(msg2)
    txtfile.write(msg3)
    txtfile.write(msg4)
    txtfile.write(msg5)
    txtfile.write(msg6)
  