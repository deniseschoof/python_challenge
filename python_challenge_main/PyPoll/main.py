import os
import csv

filename="election_data.csv"
dir_path=os.path.dirname(os.path.realpath(__file__))
#print(dir_path)
os.chdir(dir_path)
pypoll_path = os.path.join(dir_path, 'resources')
print(pypoll_path)
#print(type(pypoll_path))
os.chdir(pypoll_path)

voter_id=[]
county=[]
candidate=[]
different_candidates=[]

with open(filename, 'r') as election:
   csvreader=csv.reader(election, delimiter=',')
   next(election)
   for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
        votes=len(voter_id)
        #print(candidate)
        #find unique candidate names
        for x in candidate:
                if x not in different_candidates:
                        different_candidates.append(x)
                        #print(different_candidates)
        khanvotes=0
        correyvotes=0
        livotes=0
        otooleyvotes=0
        #print(different_candidates)
        for y in candidate:
                if candidate== "Khan":
                        khanvotes = (khanvotes +1)
                elif candidate=="Correy":
                        correyvotes=(correyvotes +1)
                elif candidate=="Li":
                        livotes=(livotes +1)                        
                elif candidate=="O'Tooley":
                        otooleyvotes=(otooleyvotes +1)
                        

        print(khanvotes)
        print(correyvotes)
        print(livotes)
        print(otooleyvotes)
                
                
                
                


#print("Total votes:" + (str(votes)))