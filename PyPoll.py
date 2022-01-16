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
# List of candidate options and candidate votes
candidate_options = []
candidate_votes = {}

# List of counties and votes
county_options = []
county_votes = {}

# Winning candidate and winning count
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Track largets county and county voter turnout
largest_turnout = ""
votes_for_county = 0
county_percentage = 0

# Open the election results and read the file. 
with open(election_data) as election_data:

# Read the file object with the reader function
    file_reader = csv.reader(election_data)

# Print the header row.
    headers = next(file_reader)

# Print each row in the CSV file.
    for row in file_reader:

        # Add to the total vote count.
        total_votes +=1

        # Print the candidate and county name from each row
        candidate_name = row[2]
        county_name = row[1]

        # Add name to candidate list.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # Begin tracking candidate vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to the count
        candidate_votes[candidate_name] +=1

        # print(candidate_votes)
        # Add name to county list.
        if county_name not in county_options:
            county_options.append(county_name)

            # Begin tracking county vote count.
            county_votes[county_name] = 0

        # Add a vote to the county
        county_votes[county_name] +=1

        # Save the results to our text file. 
with open(election_analysis, "w") as txt_file:
    election_results=(
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes:  {total_votes:,}\n"
        f"--------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)
    
    # Loop through county list.
for county_name in county_votes:

    # Get votes count for county
    votes2 = county_votes[county_name]

    # Calculate percentage
    vote_percentage2 = float(votes2) / float(total_votes) * 100
    county_results = (f"{county_name}: {vote_percentage2:.1f}%: ({votes2:,})\n")
    with open(election_analysis, "a") as txt_file:
        print(county_results, end="")
        txt_file.write(county_results)

    # Determining largest turnout
    if (votes2 > votes_for_county) and (vote_percentage2 > county_percentage):
        votes_for_county = votes2
        county_percentage = vote_percentage2
        largest_turnout = county_name

    highest_turnout_summary = (
        f"-------------------------------------\n"
        f"Largest County Turnout: {largest_turnout}\n"
        f"--------------------------------------\n")
with open(election_analysis, "a") as txt_file:
    print(highest_turnout_summary)
    txt_file.write(highest_turnout_summary)
    
# Percentage votes
    # Loop through candidate list.
for candidate_name in candidate_votes:

    # Get vote count for candidate
    votes = candidate_votes[candidate_name]

    # Calculate percentage
    vote_percentage = float(votes) / float(total_votes) * 100
          
    # Determining winner
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name  

    # Print candidate name and percentage
    with open(election_analysis, "a") as txt_file:
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")   
        print(candidate_results)
        txt_file.write(candidate_results)

    winning_candidate_summary = (
        f"-------------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------------------\n")
with open(election_analysis, "a") as txt_file:    
    print(winning_candidate_summary, end="")
    txt_file.write(winning_candidate_summary)