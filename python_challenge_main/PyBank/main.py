import os
import csv

filename="budget.csv"
dir_path=os.path.dirname(os.path.realpath(__file__))
#print(dir_path)
os.chdir(dir_path)
pybank_path = os.path.join(dir_path, 'resources')
print(pybank_path)
#print(type(pybank_path))
os.chdir(pybank_path)

month=[]
profit_loss=[]

with open(filename, 'r') as budget:
   csvreader=csv.reader(budget, delimiter=',')
   next(budget)
   for row in csvreader:
      month.append(row[0])
      profit_loss.append(int(row[1]))
      print(row)
      #print(row[0])
      net_profit = sum(profit_loss)
      number_of_months=len(month)

print("Net profit is $" + (str(net_profit)))
print("Months:" + (str(number_of_months)))

#print(min(profit_loss))
#print(max(profit_loss))
average_change=(((1, 1)-(1, 86))/number_of_months)
print("Average change is $" + (str(average_change)))

