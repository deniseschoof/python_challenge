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
votes = len(voter_id)
khanpercent = (khanvotes / votes)*100
correypercent = (correyvotes / votes)*100
lipercent = (livotes / votes)*100
otooleypercent = (otooleyvotes / votes)*100
print("Total votes:" + (str(votes)))

print("Khan: " + str(khanpercent) + "% of the votes  :" + str(khanvotes))
print("Correy: " + str(correypercent) + "% of the votes  :" + str(correyvotes) )
print("Li: " + str(lipercent) + "% of the votes  :" + str(livotes))
print("O'Tooley: " + str(otooleypercent) + "% of the votes  :" + str(otooleyvotes))

if khanvotes > correyvotes and livotes and otooleyvotes:
        print ("Khan is the winner!")
elif correyvotes > khanvotes and livotes and otooleyvotes:
        print ("Correy is the winner!")
elif livotes > khanvotes and correyvotes and otooleyvotes:
        print ("Li is the winner!")
elif otooleyvotes > khanvotes and livotes and correyvotes:
        print ("O'Tooley is the winner!")



