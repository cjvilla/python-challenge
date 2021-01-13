import os
import csv

# Change directory to the directory of current python script
current_path = os.path.dirname(os.path.abspath(__file__))
# path to .csv file
file = os.path.join('Resources', 'budget_data.csv')

#empty lists

net_cost = []
count = 0
sum = 0


# Open and read csv
with open(file, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    # Read the header row first
    csv_header = next(csv_file)
    for row in csv_reader:
     count += 1
     sum += float(row[1])
    
pattern = '-'
print(f"Financial Analysis \n{pattern * 30} ")
print(f"Total Months: {count}")
print(f"Total: {'${:.1f}'.format(sum)}")
