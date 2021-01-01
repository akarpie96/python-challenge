import os 
import csv

pybank_csv=os.path.join("..","PyBank", "Resources", "budget_data.csv")

total_months=[]
total_profit = []

difference = []
i=0 

with open (pybank_csv, 'r') as csvfile :
    csvreader=csv.reader(csvfile) 
    csvheader=next(csvreader)

    for row in csvreader:
        total_months.append(row[0])
        total_profit.append(row[1])


while i<85: 
    diff= int(total_profit[i+1]) - (int(total_profit[i]))

    difference.append(diff)

    i = i + 1
         


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
print(difference)
print("Financial Analysis")  
print("-----------------------") 
print(f"Total Months: {len(total_months)}")
print(f"Total: ${round(sum(total_profit))}")
print(f"Average Change : ${round((int(total_profit[85])-int(total_profit[0]))/((85)),2)}")
