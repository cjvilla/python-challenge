import os
import csv
import sys
import operator 
current_path = os.path.dirname(os.path.abspath(__file__))
file = os.path.join('Resources', 'election_data.csv')

def convert_to_percentage(count, sum):
    total = (count/sum) * 100
    return total

def print_election_results(election_data):
    #variables
    count = 0
    khan_count = 0
    khan_percent = 0
    correy_count = 0
    correy_percent = 0
    li_count = 0
    li_percent = 0
    otoole_count = 0
    otoole_percent = 0
    hold_candidates = [] # list of candidates
    

    with open(file, newline="") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        header = next(csv_reader)
        for row in csv_reader:
            count += 1
            hold_candidates.append(row[2])
        for i in hold_candidates:
            if i == "Khan":
                khan_count += 1
                khan_percent = convert_to_percentage(khan_count, count)
            if i == "Correy":
                correy_count += 1
                correy_percent = convert_to_percentage(correy_count, count)
            if i == "Li":
                li_count += 1
                li_percent = convert_to_percentage(li_count, count)
            if i == "O'Tooley":
                otoole_count += 1
                otoole_percent = convert_to_percentage(otoole_count, count)
        
        candidate_dict = {
            "Khan": khan_count,
            "Correy": correy_count,
            "Li": li_count,
            "O'Tooley": otoole_count
        }

    print(f"Election Results \n{'-' * 30} \nTotal Votes: {count} \n{'-' * 30}")
    print(f"Khan : {'{:.3f}'.format(khan_percent)}% ({khan_count})")
    print(f"Correy : {'{:.3f}'.format(correy_percent)}% ({correy_count})")
    print(f"Li : {'{:.3f}'.format(li_percent)}% ({li_count})")
    print(f"O'Tooley : {'{:.3f}'.format(otoole_percent)}% ({otoole_count}) \n{'-' * 30}")
    print(f"Winner: {max}")
    
    # print(set(hold_candidates)) prints unique set of candidates
print_election_results(file)
   