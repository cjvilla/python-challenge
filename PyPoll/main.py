import os
import csv
import sys

# Change directory to the directory of current python script
current_path = os.path.dirname(os.path.abspath(__file__))
file = os.path.join('Resources', 'election_data.csv')

def print_candidate_results(budget_data):
    #initialize variables
    count = 0
    w_count = 0
    candidates_dict = {}
    candidates_percentages = {}
  
    # Open and read csv
    with open(file, newline="") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        csv_header = next(csv_file)

        for row in csv_reader:
            count += 1
            if row[2] in candidates_dict.keys():
                candidates_dict[row[2]] += 1
            else:
                candidates_dict[row[2]] = 1

        for key, value in candidates_dict.items(): # convert to percentages
            candidates_percentages[key] = (value/count) * 100

        for key in candidates_dict.keys(): 
            if candidates_dict[key] > w_count:
                winner = key 
                w_count = candidates_dict[key] #total count of winning candidate
    
    print(f"Election Results \n{'-' * 30} \nTotal Votes: {count} \n{'-' * 30}")
    for key, value in candidates_dict.items():
        print(f"{key}: {'{:.3f}'.format(candidates_percentages[key])}% ({value})")
    print(f"{'-' * 30} \nWinner: {str(winner)}")


print_candidate_results(file)

output_file = os.path.join('Analysis', 'poll_analysis.txt')
sys.stdout = open(output_file, "w")
print_candidate_results(file)
sys.stdout.close()
