# Election_Analysis

## Overview
Having the poll data for the election, an analysis was completed to determine: total votes in the election, number of votes for each candidate, percentage of total votes each candidate received, and based on those results determine the winner. 

### Resources
    _ Data: election_results.csv
    _ Python; Visual Studio Code
    
## Final Results of the Poll

         Election Results
        -------------------------
         Total Votes:  369,711
        --------------------------
         Charles Casper Stockham: 23.0% 85,213
         Diana DeGette: 73.8% 272,892
         Raymon Anthony Doane: 3.1% 11,606

### Challenge Overview
Having completed the initial analysis to determine winner of the election, the request was processed to complete analysis to identify the county with the highest turnout and turnout per county. The analysis was built in such a way as to present total election information first, followed by county specifics, candidate specifics, and finally the election winner by popular vote. 

### Challenge Summary
#### Election-Audit Results:

The image included below is the output of the final run of analysis. Clearly indicating Diana DeGette as the popluar vote winnder, having received 73.8% of the total votes. 

![election results](https://github.com/RachelRautenberg/election_analysis/blob/main/analysis/election_analysis_results.PNG)

In order to acheive this, code block was started with collecting total election votes. This was done using a for loop to increment by 1 for each row, not including the header row. 

Next, an if loop with not in logic was used to collect candidate names, appending the list of candidates for each new name. Then, similar to total count, within the for loop, once candidate names were gathered, each candidated was incremented once fore every time they received a vote. A very similar section of code was run to gather county names and increment for each time the county name appeared within the data. 

#### Election-Audit Summary
This script was effective and efficient, resulting in expected output quickly. While this analysis was run with only participation of three counties and three candidates, this could easily be used for compiling statewide data.  The script is written in such a manner that we pull names of candidates and counties mitgating the need to edit script or provide a list of candidate names, for example if an electronic ballot allowed for write ins, that name would also appear in the data and show up in the results. 

Additional modifications to consider:
- In addition to writing a full results summary for the election office, county analysis could be written in a seperate file that is shared with the candidates or campaigns; it may be of interest to them to direct their campaing focus where the biggest turnout is, or possible in the lower turnout areas to increase overall voter participation.
- 

