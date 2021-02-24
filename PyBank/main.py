import os
import csv

#set path 
# path from Sal Netflix (try "" vs ""): csvpath = os.path.join(os.path.dirname(__file__),"budget_data.csv")
csvpath = os.path.join(os.path.dirname(__file__),"Resources","budget_data.csv")
#should work:
    #csvpath = os.path.join("..","PyBank","Resources","budget_data.csv")


#Set variables
total_months = 0
total_pl = 0
prev_pl = 0
month_ch = 0 
total_month_ch = 0
avg_month_ch = 0
greatest_increase = 0 
greatest_increase_month = ""
greatest_decrease = 0 
greatest_decrease_month = ""

#open and read csv
with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    #read through each row in header
    for row in csvreader:
        #count total number of months
        total_months += 1

        #total p/l
        total_pl += int(row[1])

        #change in p/l between months
        if total_months > 1:
            month_ch = int(row[1]) - prev_pl
        
        #add up the total monthly change, used to cal avg
        total_month_ch += month_ch

        #set p/l from previous month
        prev_pl = int(row[1])

        #cal greatest increase in p
        if month_ch > greatest_increase:
            greatest_increase = month_ch
            greatest_increase_month = row[0]
        
        #cal greatest decrease in p
        if month_ch < greatest_decrease:
            greatest_decrease = month_ch
            greatest_decrease_month = row[0]

#calculate avg ch between m
avg_month_ch = total_month_ch / (total_months -1)

#print analysis to terminal
print("Financial Analysis")
print("--------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(total_pl))
print("Average Change: $" + str(format(avg_month_ch, '.2f')))
print("Greatest Increase in Profits:" + greatest_increase_month + "($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits:" + greatest_decrease_month + "($" + str(greatest_decrease) + ")")

#write to text file: 
'''#from DAY 3 class recording ~41min in:
with open(csvfile) as myText:
    csvreader = csv.reader(myText, delimiter=',')

    print(csvreader):
    print(row)
'''


f = open("Analysis.txt", "w")
f.write("Financial Analysis\n")
f.write("---------------------\n")
f.write("Total Months: " + str(total_months) + "\n")
f.write("Average Change: $" + str(format(avg_month_ch, '.2f')) + "\n")
f.write("Greatest Increase in Profits:" + greatest_increase_month + "($" + str(greatest_increase) + ")\n")
f.write("Greatest Decrease in Profits:" + greatest_decrease_month + "($" + str(greatest_decrease) + ")\n")
f.close

