import os
import csv
import sys

# Change directory to the directory of current python script
current_path = os.path.dirname(os.path.abspath(__file__))
file = os.path.join('Resources', 'budget_data.csv')

def find_finances (budget_data):
    #initialize variables
    count = 0 # counts number of months
    sum = 0 # sum of profits 
    sum_change = 0 #total change
    profit_changes = [] # holds profit changes 
    max_increase = [0, count] 
    max_decrease = [0, count]

    # Open and read csv
    with open(file, newline="") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        # Read the header row first
        csv_header = next(csv_file) #header/title info
        first_row = next(csv_reader) # will iterate to next item
        prev_row = int(first_row[1])

        for row in csv_reader:
            count += 1 # number of months
            sum += float(row[1]) # total profits
            curr_row = int(row[1])
            profit_change = int(curr_row - prev_row)
            profit_changes.append(profit_change)
            prev_row = int(row[1])
            sum_change += profit_change

            if profit_change > max_increase[1]:
                max_increase[0] = str(row[0]) # month of greatest increase
                max_increase[1] = profit_change # greatest profit
            if profit_change < max_decrease[1]:
                max_decrease[0] = str(row[0]) # month of greatest decrease
                max_decrease[1] = profit_change # greatest decrease 

    average_change = sum_change/count 
    print(f"Financial Analysis \n{'-' * 30}")
    print(f"Total Months: {count} \nTotal: {'${:.1f}'.format(sum)}")
    print(f"Average Change: {'${:.2f}'.format(average_change)}")
    print(f"Greatest Increase in Profits: {max_increase[0]} ({'${:.2f}'.format(max_increase[1])}) \nGreatest Decrease in Profits: {max_decrease[0]} ({'${:.2f}'.format(max_decrease[1])}) ")

find_finances(file)

output_file = os.path.join('Analysis', 'financial_analysis.txt')
sys.stdout = open(output_file, "w")
find_finances(file)
sys.stdout.close()
