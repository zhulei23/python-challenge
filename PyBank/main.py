import os
import csv
from pathlib import Path

# Collect data from csv datafile in the resources folder

PyBank_path = os.path.join('Resources', 'budget_data.csv')
months = []
profit_loss = []
profit_loss_change = []
greatest_increase = ""
greatest_decrease = ""

# Retrieve data from csv datafile
with open(PyBank_path, 'r') as csvdatafile:
    csvreader = csv.reader(csvdatafile, delimiter = ',')
    csv_header = next(csvreader)

# Create a loop to retrieve data & append into month & profit_loss lists
    for row in csvreader:
        months.append(row[0])
        profit_loss.append(int(row[1]))

    # Count total month & total amount of profit/loss
    total_month_count = len(months)
    total_amount_profit_loss = sum(profit_loss)

    # Create a loop to calculate Average Change
    for i in range(len(profit_loss)-1):
        profit_loss_change.append(profit_loss[i+1]-profit_loss[i])

        # Calculate Greatest Increase in Profit, Greatest Decrease in Profit, Greatest Increase month, and Greatest Decrease month
        i = 0
        for i in range (1, len(profit_loss)):
            profit_loss_change.append(profit_loss[i] - profit_loss[i-1])
            greatest_increase = max(profit_loss_change)
            greatest_increase_month = str(months[profit_loss_change.index(max(profit_loss_change))])
            greatest_decrease = min(profit_loss_change)
            greatest_decrease_month = str(months[profit_loss_change.index(min(profit_loss_change))])

# Print final result for Financial Analysis
    print("Financial Analysis")
    print("------------------------")
    print("Total Months: " + str(total_month_count))
    print("Total: $" + str(total_amount_profit_loss))
    print(f"Average Change: ${round(sum(profit_loss_change)/len(profit_loss_change),2)}")
    print(f"Great Increase in Profits: {greatest_increase_month} (${greatest_increase})")
    print(f"Great Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")


# Export a text file for the final result
output_datafile = Path('Financial Analysis.txt')
with open(output_datafile,"w") as datafile:

    datafile.write("Financial Analysis" + "\n")
    datafile.write("----------------------------" + "\n")
    datafile.write("Total Months: " + str(total_month_count) + "\n")
    datafile.write("Total: $" + str(total_amount_profit_loss) + "\n")
    datafile.write(f"Average Change: ${round(sum(profit_loss_change)/len(profit_loss_change),2)} \n")
    datafile.write(f"Great Increase in Profits: {greatest_increase_month} (${greatest_increase}) \n")
    datafile.write(f"Great Decrease in Profits: {greatest_decrease_month} (${greatest_decrease}) \n")
