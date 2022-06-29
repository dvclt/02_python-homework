# pseudo code:
#     read csv file
#     interate through all rows 
#     find: total, avg, max, min
#     export to export csv

from pathlib import Path

import csv

filepath = Path("./Resources/budget_data.csv")

with open (filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    headers = next(csvreader)
    
    total_month = 0
    total = 0
    
    change = 0
    last_month = 0
    avg_change = 0
    total_change =0
    
    grt_increase = True
    grt_increase_date = 0
    
    grt_decrease = True
    grt_decrease_date = 0
    
    for row in csvreader:
        total_month += 1
        total += int(row[1])
         
        #calculate change
        if last_month ==0:
            last_month = int(row[1])
        
        change = int(row[1]) - last_month
        
        total_change +=change
        last_month = int(row[1])
        
        #find max increase:
        if change >= 0:
            if grt_increase == True:
                grt_increase = change
                grt_increase_date = row[0]
            elif change > grt_increase:
                grt_increase = change
                grt_increase_date = row[0]

        #find max decrease:
        else:
            if grt_decrease == True:
                grt_decrease = change
                grt_decrease_date = row[0]
                
            elif change < grt_decrease:
                grt_decrease = change
                grt_decrease_date = row[0]

        #note: can use max() and min(), also can create list of records        
        
    avg_change = round(total_change / (total_month-1),2)

#Print to terminal:
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {total_month}')
print(f'Total: ${total}')
print(f'Average  Change: ${avg_change}')
print(f'Greatest Increase in Profits: {grt_increase_date} (${grt_increase})')
print(f'Greatest Decrease in Profits: {grt_decrease_date} (${grt_decrease})')


#output:
output_filepath = Path('./output.txt')

with open (output_filepath, 'w') as file:
    file.write('Financial Analysis\n')
    file.write('----------------------------\n')
    file.write(f'Total Months: {total_month}\n')
    file.write(f'Total: ${total}\n')
    file.write(f'Average  Change: ${avg_change}\n')
    file.write(f'Greatest Increase in Profits: {grt_increase_date} (${grt_increase})\n')
    file.write(f'Greatest Decrease in Profits: {grt_decrease_date} (${grt_decrease})\n')
