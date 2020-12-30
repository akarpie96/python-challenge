import os 
import csv

pybank_csv=os.path.join("..","PyBank", "Resources", "budget_data.csv")

total_months=[]
total_profit = []

with open (pybank_csv, 'r') as csvfile :
    csvreader=csv.reader(csvfile) 

    for row in csvreader:
        total_months.append(row[0])
        total_profit.append(row[1])

print(total_profit)