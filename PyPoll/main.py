import os
import csv
import sys

current_path = os.path.dirname(os.path.abspath(__file__))
file = os.path.join('Resources', 'election_data.csv')

def print_election_results(election_data):
    count = 0
    hold_candidates = [] # list of candidates

    with open(file, newline="") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        header = next(csv_reader)
        for row in csv_reader:
            count += 1
            hold_candidates.append(row[2])
   
    print(f"Election Results \n{'-' * 30} \nTotal Votes: {count}")
    print(f"{len(set(hold_candidates)) - 1}") #starts at 0
    
    
    
print_election_results(file)
   