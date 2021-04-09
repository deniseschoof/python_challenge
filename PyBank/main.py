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
      number_of_months = len(month)
      max_profit = max(profit_loss)
      min_profit = min(profit_loss)
      average_change = (max_profit - min_profit) / number_of_months
           
print("Net profit is $" + (str(net_profit)))
print("Months:" + (str(number_of_months)))
print("The average change is $" + (str(average_change)))