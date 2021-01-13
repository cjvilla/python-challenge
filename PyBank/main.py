import os
import csv

# Change directory to the directory of current python script
current_path = os.path.dirname(os.path.abspath(__file__))
file = os.path.join('Resources', 'budget_data.csv')

#initialize variables
count = 0 # counts number of months
sum = 0 # counts sum of profits 
profits = []

# Open and read csv
with open(file, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    # Read the header row first
    csv_header = next(csv_file)
    for row in csv_reader:
        count += 1
        sum += float(row[1])
        profits.append(row[1])
   
pattern = '-'
print(f"Financial Analysis \n{pattern * 30} ")
print(f"Total Months: {count} \nTotal: {'${:.1f}'.format(sum)}")

