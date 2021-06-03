# PyBank
## PyBank Background
* Created a Python script for analyzing the financial records of fictional company using [Budget Data](/Resources%20-%20PyBank/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`.

* The python script calculates the following:

  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * The changes in "Profit/Losses" over the entire period, and the average of those changes. 

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period

* Final Output to both terminal and text file. 

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```

## PyPoll


* Created a Python script to auotmate vote counting process using [Election Data](/Resources%20PyPoll/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. 

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.

* As an example, your analysis should look similar to the one below:

  ```text
  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  ```

* In addition, your final script should both print the analysis to the terminal and export a text file with the results.
