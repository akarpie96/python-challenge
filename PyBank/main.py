import os 
import csv

pybank_csv=os.path.join("..", "PyBank", "budget_data.csv")

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

def max(total_profit): 
    Max = 0 
    for number in difference:
        if number>Max: 
            Max = number 
    return Max 

def min(difference):
    Min = 0 
    for number in difference: 
        if number<Min: 
            Min = number
    return Min
print("Financial Analysis")  
print("-----------------------") 
print(f"Total Months: {len(total_months)}")
print(f"Total: ${round(sum(total_profit))}")
print(f"Average Change : ${round((int(total_profit[85])-int(total_profit[0]))/((85)),2)}")
print(f"Greatest Increase in profits: (${max(difference)})")
print(f"Greatest Decrease in profits: (${min(difference)})")

output_file = os.path.join("analysis.txt")

with open(output_file, "w", newline='') as text: 

    text.write("Financial Analysis\n")
    text.write("-----------------------\n")
    text.write(f"Total Months: {len(total_months)}\n")
    text.write(f"Average Change : ${round((int(total_profit[85])-int(total_profit[0]))/((85)),2)}\n")
    text.write(f"Greatest Increase in profits: (${max(difference)})\n")
    text.write(f"Greatest Decrease in profits: (${min(difference)})")