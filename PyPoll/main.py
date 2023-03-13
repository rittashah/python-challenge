import csv
pybank_path=r"PyPoll/Resources/election_data.csv"
total_votes = 0 
Charles_Casper_votes = 0
Diana_DeGette_votes = 0
Raymon_Anthony_votes = 0

with open(pybank_path, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader: 
        total_votes +=1
        if row[2] == "Charles Casper Stockham": 
            Charles_Casper_votes +=1
        elif row[2] == "Diana DeGette":
            Diana_DeGette_votes +=1
        elif row[2] == "Raymon Anthony Doane": 
            Raymon_Anthony_votes+=1
    candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
    votes = [Charles_Casper_votes, Diana_DeGette_votes,Raymon_Anthony_votes]
    dict_candidates_and_votes = dict(zip(candidates,votes))
    key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)
    Charles_Casper_percent = (Charles_Casper_votes/total_votes) *100
    Diana_DeGette_percent = (Diana_DeGette_votes/total_votes) * 100
    Raymon_Anthony_percent = (Raymon_Anthony_votes/total_votes)* 100
    print(f"Election Results")
    print(f"----------------------------")
    print(f"Total Votes: {total_votes}")
    print(f"----------------------------")
    print(f"Charles Casper Stockham: {Charles_Casper_percent:.3f}% ({Charles_Casper_votes})")
    print(f"Diana DeGette: {Diana_DeGette_percent:.3f}% ({Diana_DeGette_votes})")
    print(f"Raymon Anthony Doane: {Raymon_Anthony_percent:.3f}% ({Raymon_Anthony_votes})")
    print(f"----------------------------")
    print(f"Winner: {key}")
    print(f"----------------------------")
    
    
    
output_file = r"PyPoll/analysis/Election_Results_Summary.txt"
with open(output_file,"w") as file:
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Charles Casper Stockham: {Charles_Casper_percent:.3f}% ({Charles_Casper_votes})")
    file.write("\n")
    file.write(f"Diana DeGette: {Diana_DeGette_percent:.3f}% ({Diana_DeGette_votes})")
    file.write("\n")
    file.write(f"Raymon Anthony Doane: {Raymon_Anthony_percent:.3f}% ({Raymon_Anthony_votes})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write(f"----------------------------")