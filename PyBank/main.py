import os 
import csv

pybank_csv=os.path.join("..", "..", "PyBank", "Resources", "budget_data.csv")

total_months=[]


with open (pybank_csv, 'r') as csvfile :
    csvreader=csv.reader(csvfile) 

    for row in csvreader:
        total_months.append(row[0])

    
print("Financial Analysis")
print("-----------------------")
print(f"Total Months: {len(total_months)}")