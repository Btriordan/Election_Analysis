
#Open the election results and read the file.
file_to_load = 'Resources\election_results.csv'

import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter
total_votes = 0
# List of counties and their votes
county_options = []
# Empty dictionary for counties and their vots
county_votes = {}
# Candidate options and candidate votes
candidate_options = []
# 1. Declare the empty dictionary.
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Largest county votes and percentage tracker
largest_county = ""
largest_count = 0
largest_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # skip the header row. 
    headers = next(file_reader)  
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1        
        # Print the candidate name from each row - in column 3.
        candidate_name = row[2]       
        if candidate_name not in candidate_options:
          # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
           # Begin tracking that candidate's vote count. 
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
        # print the county name for each row
        county_name = row[1]       
        if county_name not in county_options:
            #add the county name to the county list
            county_options.append(county_name)           
            # Track that conty's vote count
            county_votes[county_name] = 0        
        #add a vote to that county's count
        county_votes[county_name] += 1
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        F"County Votes:\n")
    print(election_results, end="")
    # Save to the txt file
    txt_file.write(election_results)
    print(county_votes)  
    for county in county_votes:
        # Get the vote count of a county
        votes = county_votes[county]
        # Calculate the percentage of votes
        county_percentage = round(int(votes) / int(total_votes) * 100,1)
        # Print each county, their voter count, and percentage to the terminal.
        county_results = (f"{county}: {county_percentage:.1f}% ({votes:,})\n")
        print(county_results)
        #  Save the county results to our text file.
        txt_file.write(county_results)
        if (votes > largest_count) and (county_percentage > largest_percentage):
            # If true then set largest_count = votes and largest_percent = vote_percentage.
            largest_count = votes
            largest_percentage = county_percentage
            # And, set the largest_county equal to the county's name.
            largest_county = county
    # Format the print how we want it to look.
    largest_county_final = (f"\n-------------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        f"-------------------------\n")
    print(largest_county_final)
    # Upload to the txt sheet.
    txt_file.write(largest_county_final)
    print(candidate_votes)
    #Iterate through the candidate list.
    for candidate in candidate_votes:
        #Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        #Calculate the percentage of votes.
        vote_percentage = round(int(votes) / int(total_votes) * 100,1)
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate
    # Summarize the winning candidate's information
    winning_candidate_summary = (f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # upload to the txt file
    txt_file.write(winning_candidate_summary)




