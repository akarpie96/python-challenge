import os 
import csv

pybank_csv=os.path.join("..","PyBank", "Resources", "budget_data.csv")

total_months=[]
total_profit = []

with open (pybank_csv, 'r') as csvfile :
    csvreader=csv.reader(csvfile) 
    csvheader=next(csvreader)

    for row in csvreader:
        total_months.append(row[0])
        total_profit.append(row[1])


def sum(total_profit): 
    length = len(total_profit)
    total = 0.0
    for number in total_profit: 
        total += float(number)
    return total 

def average(total_profit):
    length= len(total_profit)
    total = 0.0
    for number in total_profit: 
        total += float(number)
    return total/length
    
print(round(sum(total_profit)))
print(len(total_months))
print(average(total_profit))
