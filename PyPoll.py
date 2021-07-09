# Import the datetime class from the datetime module.
import datetime
import csv
import os
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()

# Print the present time.
print("The time right now is ", now)
#print(dir(csv))
# Open the data file.
# Open the election results and read the file.
file_to_load = os.path.join("Resources", "election_results.csv")
election_data = open(file_to_load, 'r')

# To do: perform analysis.

# Close the file.
election_data.close()


# Assign a variable for the file to load and the path.

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)

file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Counties in the Election\n")
    txt_file.write("------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")

    
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
# Write down the names of all the candidates.
# Add a vote count for each candidate.
# Get the total votes for each candidate.
# Get the total votes cast for the election.