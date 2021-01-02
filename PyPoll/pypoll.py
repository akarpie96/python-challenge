import os 
import csv 

total_vote=[]
totalvotecount=len(total_vote)
khanvote= 0 
Correyvote= 0 
Livote= 0 
Otooleyvote= 0
csvfilepath=os.path.join("..", "..", "PyPoll", "Resources", "election_data.csv" )

with open(csvfilepath, "r") as csvfile: 
    csvreader=csv.reader(csvfile, delimiter=',')
    csvheader=next(csvreader)
    print(csvheader)

    for row in csvreader: 
        total_vote.append(row[2])
    
#Conditional statement to find total votes of each candidate within appended list 'total_row' 
    for row in total_vote: 
        if row=="Khan":
            khanvote= khanvote+1
        elif row=="Correy":
            Correyvote= Correyvote+1 
        elif row=="Li":
            Livote = Livote+1

        elif row== "O'Tooley":
            Otooleyvote=Otooleyvote+1
    




totalvotecount=len(total_vote)
khanpercentage= khanvote/totalvotecount 
correypercentage= Correyvote/totalvotecount
Lipercentage= Livote/totalvotecount
Otooleypercentage= Otooleyvote/totalvotecount
#Total Votes cast 
print(totalvotecount)

# Total Votes cast for each candidate 
print(khanvote)
print(Correyvote)
print(Livote)
print(Otooleyvote)
# Percentage of total votes cast for each candidate/applying formatting to variables for simplicity
Khan_percent=("{:.3%}".format(khanpercentage))
Correy_percent=("{:.3%}".format(correypercentage))
Li_percent=("{:.3%}".format(Lipercentage))
Otooley_percent=("{:.3%}".format(Otooleypercentage))


#Final Result 
print("Election Results")
print("-----------------------")
print(f"Total Votes: {totalvotecount}")
print("-----------------------")
print(f"Khan: {Khan_percent} ({khanvote})")
print(f"Correy: {Correy_percent} ({Correyvote})")
print(f"Li: {Li_percent} ({Livote})")
print(f"O'Tooley: {Otooley_percent} ({Otooleyvote})")