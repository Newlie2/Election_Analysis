



# print("hello world")

# counties = ["Arapahoe", "Denver", "Jefferson"]  
# if counties == 0:
#     print("Arapahoe")
# if counties == 1:
#     print("Denver")
# if counties == 2:
#     print("Jefferson")
# len (counties)

# counties.append("El paso")

# print("counties")
    
    
# counties_tuple =("Arapahoe", "Denver", "Jefferson")
# len(counties_tuple)
# 3

# counties_tuple[1]
# "Denver"


#  Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# file_to_load = os.path("Resources/election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")


# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.

candidate_options = []
candidate_votes = {}
counties_dict = {}

# 1: Create a county list and county votes dictionary.
# len(counties_dict)

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.


# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # For each row in the CSV file.
    for row in file_reader:

        # Add to the total vote count
        total_votes = total_votes + 1
       

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.


        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 1
        else:

        # Add a vote to that candidate's count
            candidate_votes[candidate_name] += 1
    for name in candidate_options:
        vote = candidate_votes.get(name)
        percentage = ((vote / total_votes) *100)

        if (vote > winning_count) and (percentage > winning_percentage):
        # if true then set winning_count = votes and winning_percent = 
         percentage
         winning_count = vote
         winning_percentage = percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = name

        print (f" {name}: {vote}, {percentage:.2f}%")
    # print(f"{name}: {percentage:.1f}% ({vote:,})\n")

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.


        # if (vote > winning_count) and (percentage > winning_percentage):
        #  If true then set winning_count = votes and winning_percent =
        #  vote_percentage.
        #  winning_count = vote
        #  winning_percentage = percentage
        #  # And, set the winning_candidate equal to the candidate's name.
        #  winning_candidate = candidate_name


            # 4b: Add the existing county to the list of counties.


            # 4c: Begin tracking the county's vote count.


        # 5: Add a vote to that county's vote count.
    # print (candidate_votes, total_votes)


# # Save the results to our text file.
# with open(file_to_save, "w") as txt_file:

#     # Print the final vote count (to terminal)
#     election_results = (
#         f"\nElection Results\n"
#         f"-------------------------\n"
#         f"Total Votes: {total_votes:,}\n"
#         f"-------------------------\n\n"
#         f"County Votes:\n")
#     print(election_results, end="")

#     txt_file.write(election_results)

#     # 6a: Write a for loop to get the county from the county dictionary.
#     counties_dict ["Arapahoe"] = 422829
#     counties_dict["Denver"] = 463353
#     counties_dict["Jefferson"] = 432438

#         # 6b: Retrieve the county vote count.
# counties_dict.items(dict_items([("A0rapahoe", 422829), ("Denver", 463353) ("Jefferson", 432438)]))
       
#         # 6c: Calculate the percentage of votes for the county.
# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                 {"county":"Denver", "registered_voters": 463353},
#                 {"county":"Jefferson", "registered_voters": 432438}]

# for county_dict in voting_data:
#     print(county_dict)

#          # 6d: Print the county results to the terminal.
# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)
        
#          # 6e: Save the county votes to a text file.

#          # 6f: Write an if statement to determine the winning county and get its vote count.
# winning_candidate_summary = (
#     f"-------------------------\n"
#     f"Winner: {winning_candidate}\n"
#     f"Winning Vote Count: {winning_count:,}\n"
#     f"Winning Percentage: {winning_percentage:.1f}%\n"
#     f"-------------------------\n")
# print(winning_candidate_summary)

#     # 7: Print the county with the largest turnout to the terminal.


#     # 8: Save the county with the largest turnout to a text file.

# counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
# for county, voters in counties_dict.items():
#     print(county + " county has " + str(voters) + " registered voters.")
#     # Save the final candidate vote count to the text file.
#     for candidate_name in candidate_votes:

#         # Retrieve vote count and percentage
#         votes = candidate_votes.get(candidate_name)
#         vote_percentage = float(votes) / float(total_votes) * 100
#         candidate_results = (
#             f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

#         # Print each candidate's voter count and percentage to the

#         print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

#         # terminal.
#         print(candidate_results)
#         #  Save the candidate results to our text file.
#         txt_file.write(candidate_results)

#         # Determine winning vote count, winning percentage, and candidate.
#         if (votes > winning_count) and (vote_percentage > winning_percentage):
#             winning_count = votes
#             winning_candidate = candidate_name
#             winning_percentage = vote_percentage

#     # Print the winning candidate (to terminal)
#     winning_candidate_summary = (
#         f"-------------------------\n"
#         f"Winner: {winning_candidate}\n"
#         f"Winning Vote Count: {winning_count:,}\n"
#         f"Winning Percentage: {winning_percentage:.1f}%\n"
#         f"-------------------------\n")
#     print(winning_candidate_summary)

#     # Save the winning candidate's name to the text file
#     txt_file.write(winning_candidate_summary)
