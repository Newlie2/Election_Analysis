# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

## Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes.
candidate_options = []
candidate_votes = {}
# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0


county_options =[]
county_votes = {}
Largest_county = ""
# largest_percentage =0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for col in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = col[2]
        # If the candidate does not match any existing candidate, add the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        county_name = col[1]

        if county_name not in county_options:
            county_options.append(county_name)
            county_votes[county_name] = 0
        county_votes[county_name] +=1
    print(county_name, county_votes, end="")
        
        


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)
    

    print (f"\nCounty Votes\n")
    txt_file.write(f"\nCounty Votes\n")
    
    for county_name in county_votes:
        # Retrieve vote count and percentage.
        votes = county_votes[county_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        county_results = (
          
            f"{county_name}: {vote_percentage:4.1f}% ({votes:,})\n")
        
         # Print each candidate's voter count and percentage to the terminal.
        print(county_results)
        txt_file.write(county_results)
        
        if (votes > winning_count) and (vote_percentage > winning_percentage):
        # if true then set winning_count = votes and winning_percent = 
        #  percentage
         winning_count = votes
         Largest_county= county_name

        
    county_Largestcounty = (
             f"\nLargest County Turnout {Largest_county}\n"
            f"-------------------------\n")

    print(county_Largestcounty)
    txt_file.write(county_Largestcounty)
    
    
       
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        cvotes = candidate_votes[candidate_name]
        cvote_percentage = float(cvotes) / float(total_votes) * 100
        candidate_results = (
                        f"{candidate_name}: {cvote_percentage:4.1f}% ({cvotes:,})\n")
        
   
        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        # print (f"-------------------------\n")
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
   
        if (cvote_percentage > winning_percentage):
      
         winning_count = cvotes
         winning_percentage = cvote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name
   
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
