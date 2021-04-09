import os
import csv
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
os.chdir(dir_path)
csvpath = os.path.join('Resources','election_data.csv')
candidate=[]
different_candidates=[]
voter_id = []
khanvotes=0
correyvotes =0
livotes = 0
otooleyvotes = 0
with open(csvpath, 'r',encoding="utf8") as election:
        
        csvreader=csv.reader(election, delimiter=',')
   
        next(election)
        
        for row in csvreader:
                candidate.append(row[2])
                voter_id.append(row[0])
        
        for i in candidate:     
                if i not in different_candidates:
                        different_candidates.append(i)     
        for x in candidate:
                if x == "Khan":
                        khanvotes = (khanvotes +1)
                elif x=="Correy":
                      correyvotes=(correyvotes +1)
                elif x=="Li":
                        livotes=(livotes +1)                        
                elif x == "O'Tooley":
                        otooleyvotes=(otooleyvotes +1)
votes=len(voter_id)
khanpercent=(votes/khanvotes)*100
correypercent=(votes/correyvotes)*100
lipercent=(votes/livotes)*100
otooleypercent=(votes/otooleyvotes)*100
print("Total votes:" + (str(votes)))
print("Khan: " + (str(khanpercent) + "% of the votes  ")+(str(khanvotes)))
print("Correy: " + str(correyvotes) + str(correypercent) + "% of the votes")
print("Li: " +(str(livotes)+ (str(lipercent) + "% of the votes")))
print("O'Tooley: " +(str(otooleyvotes)+ (str(otooleypercent) + "% of the votes")))
print("The Winner is TODO")



