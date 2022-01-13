# Import the datetime class from the datetime module
import datetime as dt
#Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is", now)

# Add dependencies
import csv
import os

# Assign a variable for the file to load and the path.
election_data = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
election_analysis = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0
# List of candidates
candidate_options = []
# Declare the empty dictionary
candidate_votes = {}
# Winning candidate and winning count
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file. 
with open(election_data) as election_data:
    # To do: read and analyze the data here

# Read the file object with the reader function
    file_reader = csv.reader(election_data)

# Print the header row.
    headers = next(file_reader)

# Print each row in the CSV file.
    for row in file_reader:

        # Add to the total vote count.
        total_votes +=1

        # Print the candidate name from each row
        candidate_name = row[2]

        # Add name to candidate list.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # Begin tracking candidate vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to the count
        candidate_votes[candidate_name] +=1

# Print the candidate list.
        print(candidate_votes)

# Percentage votes
# Loop through candidate list.
for candidate_name in candidate_votes:

    # Get vote count for candidate
    votes = candidate_votes[candidate_name]

    # Calculate percentage
    vote_percentage = float(votes) / float(total_votes) * 100
    
    # Print candidate name and percentage
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determining winner
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name
    
winning_candidate_summary = (
    f"-------------------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"--------------------------------------\n")
print(winning_candidate_summary)

# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote